

from flask_login import UserMixin
from .app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from flask_migrate import Migrate
import hashlib


db = SQLAlchemy(app)
migrate = Migrate(app, db)
class User(UserMixin, db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fname= db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    pwd_hash = db.Column(db.String(128))
    phone_num = db.Column(db.String(13), nullable = False)
    tickets = db.relationship('Ticket', backref= 'raised_by_user', foreign_keys='Ticket.raised_by')
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")
    @password.setter
    def password(self, password):
        self.pwd_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    def verify_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest() == self.pwd_hash
    
    def get_id(self):
        return str(self.user_id)
    def __repr__(self):
        return f'<User {self.email}>'
    

class Admin(UserMixin, db.Model):
    __tablename__ = "admin"
    emp_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fname= db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    pswd = db.Column(db.String(100), nullable = False)
    phone_num = db.Column(db.String(13), nullable = False)
    dept = db.Column(db.String(25), nullable = False)
    tickets = db.relationship('Ticket', backref= 'assigned_to_admin', foreign_keys='Ticket.assigned_to')

    def __repr__(self):
        return f'<Admin {self.email}>'
    
    
class Ticket(db.Model):
    __tablename__ = "ticket"
    ticket_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title= db.Column(db.String(100), nullable = False)
    body = db.Column(db.String(200), nullable = False)
    raised_by = db.Column(db.String(36), db.ForeignKey('user.user_id'),nullable = False)
    assigned_to = db.Column(db.String(36), db.ForeignKey('admin.emp_id'),nullable = False)
    created_at= db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    def __repr__(self):
        return f'<Ticket {self.title}>'
    
