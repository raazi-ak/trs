from __future__ import annotations
import os
from flask import Flask, render_template, render_template_string, request, url_for
from flask_restful import Api


basedir = os.path.abspath(os.path.dirname(__file__))

app =  Flask(__name__)
api = Api(app)



app.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.config['SECRET_KEY'] = 'gnKRCJ3jmXqHiIcKHrGkByfReiyQTVP7'
from .models import db

def initDB():
    app.app_context().push()
    db.create_all()
    

initDB()

from .views import home
from .login import get_all_users
from .login import get_user
from .login import register_user
from .login import login