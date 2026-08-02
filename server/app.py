#!/usr/bin/env python3

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from models import db, bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'change-this-later-for-real-use'

migrate = Migrate(app, db)

db.init_app(app)
bcrypt.init_app(app)
api = Api(app)

# Routes go here - we'll add these next

if __name__ == '__main__':
    app.run(port=5555, debug=True)