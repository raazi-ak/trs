from flask import jsonify, request
from flask_login import LoginManager
from .models import User
from .models import db
from .app import app

from flask_restful import Resource, Api, reqparse
from flask_login import LoginManager, UserMixin, login_user, login_required

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not all(field in data for field in ['email', 'password']):
        return jsonify({'message': 'Missing required fields'}), 400

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({'message':'User does not exist'})
    elif not user.verify_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    

    # Login successful 
    return jsonify({'message': 'Login successful'}), 200

@app.route('/register', methods = ['POST'])
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
    
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_data = []
    for user in users:
        user_data.append({'user_id': user.user_id, 'fname': user.fname, 'lname': user.lname, 'email': user.email})
    return jsonify(user_data)

# Get a specific user by ID route
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user_id': user.user_id, 'fname': user.fname, 'lname': user.lname, 'email': user.email})