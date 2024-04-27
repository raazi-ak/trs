from flask import jsonify
from .app import app
from flask_restful import Api, Resource
from .response_schema import admin_schema
from .response_schema import admins_schema
from .response_schema import ticket_schema
from .response_schema import tickets_schema
from .response_schema import user_schema
from .response_schema import users_schema
from .models import User
from .models import Admin
from .models import Ticket
from .response_schema import marshmallow



api = Api(app)

@app.route('/users/')
def user_list():
    try:
        all_users = User.query.all()
        print(all_users)
        response = jsonify(users_schema.dump(all_users))
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

    if not all_users:
        return jsonify({"message": "No users found."}), 404

    return response
@app.route('/admins/')
def admin_list():
    try:
        all_admins = Admin.query.all()
        print(all_admins)
        response = jsonify(users_schema.dump(all_admins))
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

    if not all_admins:
        return jsonify({"message": "No users found."}), 404

    return response