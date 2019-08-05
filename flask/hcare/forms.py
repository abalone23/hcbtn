from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class PredictForm(FlaskForm):
    state = SelectField(u'State',
                             choices=[('s', 'Select State'), ('ak', 'Alaska'), ('al', 'Alabama'), ('ar', 'Arkansas'), ('az', 'Arizona'),
                                      ('ca', 'California'), ('co', 'Colorado'), ('ct', 'Connecticut'), ('de', 'Delaware'), ('fl', 'Florida'),
                                      ('ga', 'Georgia'), ('hi', 'Hawaii'), ('ia', 'Iowa'), ('id', 'Idaho'), ('il', 'Illinois'), ('in', 'Indiana'),
                                      ('ks', 'Kansas'), ('ky', 'Kentucky'), ('la', 'Louisiana'), ('ma', 'Massachusetts'), ('md', 'Maryland'),
                                      ('me', 'Maine'), ('mi', 'Michigan'), ('mn', 'Minnesota'), ('mo', 'Missouri'), ('ms', 'Mississippi'),
                                      ('mt', 'Montana'), ('nc', 'North Carolina'), ('nd', 'North Dakota'), ('ne', 'Nebraska'), ('nh', 'New Hampshire'),
                                      ('nj', 'New Jersey'), ('nm', 'New Mexico'), ('nv', 'Nevada'), ('ny', 'New York'), ('oh', 'Ohio'), ('ok', 'Oklahoma'),
                                      ('or', 'Oregon'), ('pa', 'Pennsylvania'), ('ri', 'Rhode Island'), ('sc', 'South Carolina'), ('sd', 'South Dakota'),
                                      ('tn', 'Tennessee'), ('tx', 'Texas'), ('ut', 'Utah'), ('va', 'Virginia'),
                                      ('vt', 'Vermont'), ('wa', 'Washington'), ('wi', 'Wisconsin'), ('wv', 'West Virginia'), ('wy', 'Wyoming')],
                                      validators=[DataRequired()])
    age = SelectField(u'Age',
                             choices=[('a', 'Select Age'), ('young_adult', 'Young Adult (< 26)'), 
                                      ('adult', 'Adult (26 - 64)'), ('senior', 'Senior (65+)')],
                                      validators=[DataRequired()])
    gender = SelectField(u'Gender',
                             choices=[('g', 'Select Gender'), ('female', 'Female'), 
                                      ('male', 'Male')],
                                      validators=[DataRequired()])
    race = SelectField(u'Race',
                             choices=[('r', 'Select Race'), ('white', 'White'), 
                                      ('black', 'Black'), ('asian', 'Asian'), ('other', 'Other')],
                                      validators=[DataRequired()])
    education = SelectField(u'Education',
                             choices=[('e', 'Select Education'), ('middle_school', 'Middle School'), 
                                      ('high_school', 'High School'), ('some_college', 'Some College'),
                                      ('college', 'College'), ('grad_school', 'Grad School'), ('other', 'Other')],
                                      validators=[DataRequired()])
    income = SelectField(u'Income',
                             choices=[('i', 'Select Income'), ('lower', 'Lower (< $40K)'), 
                                      ('middle', 'Middle ($40K - $90K)'), ('upper', 'Upper (> $90K)')],
                                      validators=[DataRequired()])
    citizen = SelectField(u'Citizen',
                             choices=[('c', 'Select Citizenship'), ('not_citizen', 'Not Citizen'), 
                                      ('other', 'Other')],
                                      validators=[DataRequired()])
    english_ability = SelectField(u'Select English Ability',
                             choices=[('ea', 'Select English Ability'), ('fluent_english', 'Fluent English'), 
                                      ('poor_english', 'Poor English'), ('no_english', 'No English'), ('other', 'Other')],
                                      validators=[DataRequired()])
    employment = SelectField(u'Employment Status',
                             choices=[('es', 'Select Employment Status'), ('employed', 'Employed'), 
                                      ('unemployed', 'Unemployed'), ('notinforce', 'Not in Labor Force')],
                                      validators=[DataRequired()])
    marital_status = SelectField(u'Marital Status',
                             choices=[('ms', 'Select Marital Status'), ('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')],
                             validators=[DataRequired()])
    submit = SubmitField('Check')