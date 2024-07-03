from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import random
import string
from datetime import datetime, timedelta

app = Flask(__name__)
app.app_context().push()
CORS(app)

app.config['SECRET_KEY'] = 'your_secret_key'
basedir = os.path.abspath(os.path.dirname(__file__))+"/db/"
if not os.path.exists(basedir):
    os.makedirs(basedir)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'link_shortener.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class URLShortener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow() + timedelta(days=30))



def generate_short_url():
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        # Ensure short_url is unique
        while URLShortener.query.filter_by(short_url=short_url).first() is not None:
            short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url


