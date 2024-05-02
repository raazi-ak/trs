import random
from flask import jsonify, request
from flask_login import LoginManager
from models import Admin, Ticket
from models import db
from app import app
from app import jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restful import Resource, Api, reqparse
from flask_login import LoginManager, UserMixin, login_user, login_required
from response_schema import ticket_schema
from response_schema import tickets_schema
#Create a new ticket
@app.route('/tickets/create', methods = ['POST'])
@jwt_required()
def create_ticket():
    identity = get_jwt_identity()
    type = identity['user_type']
    if not  type == 'user':
        return jsonify({'message': 'invalid account type. operation disabled.'})
    

    user_id = identity['user_id']
    data = request.get_json()
    if not data or not all(field in data for field in ['title', 'body']):
        return jsonify({'message': 'Missing required fields'}), 400
    title = data['title']
    body  =  data['body']
    admin_count = Admin.query.count()
    random_admin =  random.randint(1, admin_count)
    ticket  = Ticket(title = title, body = body, raised_by = user_id, assigned_to = random_admin)
    db.session.add(ticket)
    db.session.commit()
    ticket_data  = ticket_schema.dump(ticket)
    return jsonify(ticket_data), 200
#Fetch existing tickets by user or emp id
@app.route('/tickets/get/byuser', methods = ['GET'])
@jwt_required()
def get_tickets():
    identity = get_jwt_identity()
    type = identity['user_type']
    id = identity['user_id'] if type == 'user' else identity['emp_id']
    query = Ticket.query
    if type == 'admin':
        query = query.filter(Ticket.assigned_to == id)
    elif type == 'user':
        query = query.filter(Ticket.raised_by == id)
    tickets= query.all()
    tickets_data = tickets_schema.dump(tickets)
    return jsonify(tickets_data), 200



