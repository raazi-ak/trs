from flask import jsonify, request
from flask_login import LoginManager
from models import Admin
from models import db
from app import app
from app import jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restful import Resource, Api, reqparse
from flask_login import LoginManager, UserMixin, login_user, login_required
from response_schema import admin_schema



@app.route('/admins/login', methods=['POST'])
def login_admin():
    data = request.get_json()

    if not data or not all(field in data for field in ['email', 'password']):
        return jsonify({'message': 'Missing required fields'}), 400

    email = data['email']
    password = data['password']

    admin = Admin.query.filter_by(email=email).first()

    if not admin:
        return jsonify({'message':'Admin does not exist'}), 401
    elif not admin.verify_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401
    

    # Login successful
    user_claims = {'emp_id': admin.emp_id, 'user_type': 'admin'}
    access_token = create_access_token(identity= user_claims)
    return jsonify({'access_token':f'{access_token}', 'message':'logged in successfully', 'account_type':'admin'}), 200

@app.route('/admins/register', methods = ['POST'])
def register_admin():
    data = request.get_json()
    if not data or not all(field in data for field in ['fname', 'lname', 'email', 'password', 'phone_num', 'dept']):
        return jsonify({'message': 'Missing required fields'}), 400
    email = data['email']
    existing_admin = Admin.query.filter_by(email=email).first()
    if existing_admin:
        return jsonify({'message': 'Email already exists'}), 400
    admin = Admin(
        fname= data['fname'],
        lname = data['lname'],
        email = data['email'],
        phone_num  =data['phone_num'],
        dept = data['dept']
    )
    admin.password = data['password']

    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify({'message': 'Admin created successfully'}), 201
    except Exception as e:
        return jsonify({'message': f'Registration failed: {str(e)}'}), 400
    

@app.route('/admins/get', methods = ['GET'])
@jwt_required()
#protected route
def get_cadmin():
    identity = get_jwt_identity()
    type = identity['user_type']
    if not type == 'admin':
        return jsonify({'message': 'not authorised for user account type'})
    emp_id= identity['emp_id']
    admin = Admin.query.get(emp_id)
    
    
    admin_data = admin_schema.dump(admin)
    return jsonify(admin_data), 200
# Get a specific user by ID route
#@app.route('/users/<int:user_id>', methods=['GET'])
#def get_user(user_id):
 #   user = User.query.get(user_id)
  #  if not user:
   #     return jsonify({'message': 'User not found'}), 404
    #return jsonify({'user_id': user.user_id, 'fname': user.fname, 'lname': user.lname, 'email': user.email})