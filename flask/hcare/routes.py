from hcare import app
from flask import render_template, url_for, flash, redirect, request
from hcare.models import States, Senators
from hcare.forms import PredictForm
import numpy as np
import pandas as pd
import psycopg2 as pg
import pickle
from collections import OrderedDict, Counter
import sklearn
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

@app.route("/map")
def map():
    # states_list = pickle.load(open(f'data/states_geo.pkl', "rb"))
    # choropleth = hv.Polygons(states_list, ['lons', 'lats'], ['state', 'tot', 'unemployed'])

    # choropleth.opts(
    # opts.Polygons(logz=True, tools=['hover'], xaxis=None, yaxis=None,
    #                show_grid=False, show_frame=False, width=830, height=500,
    #                color_index='tot', cmap='Oranges', colorbar=True, toolbar='above', line_color='white'))

    return render_template('map.html',
                            title='Health Care by the Numbers Map')

@app.route("/")
def index():
    mystates = States.query.order_by(States.state)
    
    states_list = pickle.load(open(f'data/states_geo.pkl', "rb"))
    choropleth = hv.Polygons(states_list, ['lons', 'lats'], ['state', 'tot', 'unemployed'])

    choropleth.opts(
    opts.Polygons(logz=True, tools=['hover'], xaxis=None, yaxis=None,
                   show_grid=False, show_frame=False, width=830, height=500,
                   color_index='tot', cmap='Oranges', colorbar=True, toolbar='above', line_color='white'))

    return render_template('index.html',
                            title='Health Care by the Numbers',
                            mystates=mystates)

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    form = PredictForm()
    if form.validate_on_submit():
        if form.age.data == 'a' or form.gender.data == 'g' or form.race.data == 'r' or form.education.data == 'e' or \
        form.income.data == 'i' or form.english_ability.data == 'ea' or form.employment.data == 'es' or form.marital_status.data == 'ms' or \
        form.state.data == 's':
            flash(f'Please fill out all options', 'danger')
        else:
            a_adult = a_senior = 0
            if form.age.data == 'adult':
                a_adult = 1
            elif form.age.data == 'senior':
                a_senior = 1

            g_male = 0
            if form.gender.data == 'male':
                g_male = 1

            r_black = r_other = r_white = 0
            if form.race.data == 'black':
                r_black = 1
            elif form.race.data == 'other':
                r_other = 1
            elif form.race.data == 'white':
                r_white = 1

            e_middle_school = e_high_school = e_college = e_some_college = e_grad_school = e_other = 0
            if form.education.data == 'middle_school':
                e_middle_school = 1
            elif form.education.data == 'high_school':
                e_high_school = 1
            elif form.education.data == 'some_college':
                e_some_college = 1
            elif form.education.data == 'grad_school':
                e_grad_school = 1
            elif form.education.data == 'other':
                e_other = 1

            i_middle = i_upper = 0
            if form.income.data == 'middle':
                i_middle = 1
            elif form.income.data == 'upper':
                i_upper = 1

            c_other = 0
            if form.citizen.data == 'other':
                c_other = 1

            ea_no_english = ea_poor_english = ea_english= 0
            if form.english_ability.data == 'no_english':
                ea_no_english = 1
            elif form.english_ability.data == 'poor_english':
                ea_poor_english = 1
            elif form.english_ability.data == 'english':
                ea_english = 1

            es_unemployed = es_notinforce = 0
            if form.employment.data == 'unemployed':
                es_unemployed = 1
            elif form.employment.data == 'notinforce':
                es_notinforce = 1

            ms_single = ms_divorced = 0
            if form.employment.data == 'single':
                ms_single = 1
            elif form.employment.data == 'divorced':
                ms_divorced = 1

            formdata = OrderedDict({'sex_male': g_male, 'marst_divorced': ms_divorced, 'marst_single': ms_single,
                'race_black': r_black, 'race_other': r_other, 'race_white': r_white, 'citizen_other': c_other,
                'speakeng_no_english': ea_no_english, 'speakeng_poor_english': ea_poor_english, 'educ_grad_school': e_grad_school,
                'educ_high_school': e_high_school, 'educ_middle_school': e_middle_school, 'educ_other': e_other,
                'educ_some_college': e_some_college, 'empstat_not_in_labor_force': es_notinforce, 'empstat_unemployed': es_unemployed,
                'incbrack_middle_income': i_middle, 'incbrack_upper_income': i_upper, 'agebrack_adult': a_adult,
                'agebrack_senior': a_senior, 'party_cnt_full_r': 1, 'party_cnt_split': 0})
            X = pd.DataFrame([formdata])

            model = pickle.load(open(f'data/model_{form.state.data}.pkl', "rb"))
            pliklihood = model.predict_proba(X)[0][0]

            hcresult = int(round(pliklihood * 100))

            return render_template('result.html',
                                    title='Predict Health Care Results', data=hcresult)
    return render_template('predict.html',
                            title='Predict Health Care Status',
                            form=form)

@app.route("/result")
def result():
    return render_template('result.html',
                            title='Predict Results', predresult=hcresult)

@app.route("/states/<state_abbr>")
def state(state_abbr):
    mystate = States.query.filter_by(state_abbr=state_abbr)
    return render_template('state.html', title='State', mystate=mystate, abbr=state_abbr)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/terms")
def terms():
    return render_template('terms.html', title='Terms')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html', title='Privacy')

@app.route("/citation")
def citation():
    return render_template('citation.html', title='Citation')