
from .models import User
from .models import Admin
from .models import Ticket
from .models import db
from .app import app
from flask import Flask, jsonify, render_template, request, url_for


@app.route('/index/')
def index():
    app.app_context().push()
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

