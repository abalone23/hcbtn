from hcare import db

class Senators(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state_abbr = db.Column(db.String(2), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    statefip = db.Column(db.Integer, nullable=False)
    party = db.Column(db.String(1), nullable=False)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Senators('{self.state_abbr}', '{self.state}', '{self.statefip}', '{self.party}', '{self.fname}, '{self.lname})"

class States(db.Model):
    statefip = db.Column(db.Integer, primary_key=True)
    state_abbr = db.Column(db.String(2), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    pct_uninsured_tot = db.Column(db.Float(4), nullable=True)
    pct_uninsured_empstat_unemployed = db.Column(db.Float(4), nullable=True)
    pct_uninsured_educ_middle_school = db.Column(db.Float(4), nullable=True)
    pct_uninsured_divinyr_yes = db.Column(db.Float(4), nullable=True)
    pct_uninsured_marst_divorced = db.Column(db.Float(4), nullable=True)
    pct_uninsured_incbrack_low_income = db.Column(db.Float(4), nullable=True)

    def __repr__(self):
        return f"States('{self.state_abbr}', '{self.state}', '{self.statefip}', '{self.pct_uninsured}')"