from __future__ import annotations
import os
from flask import Flask, render_template, render_template_string, request, url_for
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint



basedir = os.path.abspath(os.path.dirname(__file__))

app =  Flask(__name__)
api = Api(app)
jwt = JWTManager(app)


app.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '$SECRET_KEY'
app.config['JWT_SECRET_KEY'] = '$JWT_SECRET_KEY'
SWAGGER_URL="/swagger"
API_URL="/static/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
from models import db

def initDB():
    app.app_context().push()
    db.create_all()
    


from views import home
from user_login import register_user
from user_login import login_user
from user_login import get_cuser
from admin_login import get_cadmin
from admin_login import login_admin
from admin_login import register_admin
from ticket_view import create_ticket
from ticket_view import get_tickets


if __name__ == '__main__':
  initDB() 
  app.run(debug=True)