from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')

POSTGRES = {
    'user': 'user',
    'pw': 'pass',
    'db': 'db',
    'host': 'host',
    'port': 'port',
}

app.config['SECRET_KEY'] = 'abc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@host/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

from hcare import routes
