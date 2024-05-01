from flask import jsonify, request
from flask_login import LoginManager
from .models import Ticket, User
from .models import Admin
from .models import db
from .app import app
from .app import jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restful import Resource, Api, reqparse
from flask_login import LoginManager, UserMixin, login_user, login_required
from .response_schema import user_schema
from .response_schema import admin_schema
from .response_schema import ticket_schema
import random


@app.route('/users/login', methods=['POST'])
def login_user():
    data = request.get_json()

    if not data or not all(field in data for field in ['email', 'password']):
        return jsonify({'message': 'Missing required fields'}), 400

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message':'User does not exist'}), 401
    elif not user.verify_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    

    # Login successful
    user_claims = {'user_id': user.user_id, 'user_type': 'user'}
    access_token = create_access_token(identity= user_claims)
    return jsonify({'access_token':f'{access_token}', 'message':'logged in successfully', 'account_type':'user'}), 200

@app.route('/users/register', methods = ['POST'])
def register_user():
    data = request.get_json()
    if not data or not all(field in data for field in ['fname', 'lname', 'email', 'password', 'phone_num']):
        return jsonify({'message': 'Missing required fields'}), 400
    email = data['email']
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400
    user = User(
        fname= data['fname'],
        lname = data['lname'],
        email = data['email'],
        phone_num  =data['phone_num']
    )
    user.password = data['password']

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': f'Registration failed: {str(e)}'}), 400
    
#@app.route('/users', methods=['GET'])
#def get_all_users():
#    users = User.query.all()
#    user_data = []
#    for user in users:
#        user_data.append({'user_id': user.user_id, 'fname': user.fname, 'lname': user.lname, 'email': user.email})
#    return jsonify(user_data)
@app.route('/users/get', methods = ['GET'])
@jwt_required()
#protected route
def get_cuser():
    identity = get_jwt_identity()
    type = identity['user_type']
    if not  type == 'user':
        return jsonify({'message': 'not authorised'})

    user_id = identity['user_id']
    user = User.query.get(user_id)

    
    

    user_data = user_schema.dump(user)
    return jsonify(user_data), 200
# Get a specific user by ID route
#@app.route('/users/<int:user_id>', methods=['GET'])
#def get_user(user_id):
 #   user = User.query.get(user_id)                 
  #  if not user:
   #     return jsonify({'message': 'User not found'}), 404
    #return jsonify({'user_id': user.user_id, 'fname': user.fname, 'lname': user.lname, 'email': user.email})