
from .models import User
from .models import Admin
from .models import Ticket
from .models import db
from .app import app
from flask import Flask, render_template, request, url_for


@app.route('/')
def index():
    app.app_context().push()
    users = User.query.all()
    return render_template('index.html', users=users)

