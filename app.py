from __future__ import annotations
import os
from flask import Flask, render_template, render_template_string, request, url_for


basedir = os.path.abspath(os.path.dirname(__file__))

app =  Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
