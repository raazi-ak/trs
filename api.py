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

api = Api(app)

class UserResource(Resource):
    def getUser(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user_schema.dump(user), 200
        return {'message': 'User not found'}, 404
    def getUsers(self):
        users = User.query.all()
        if users:
            return users_schema.dump(users), 200
        return {'message': "coulnd't retrieve users"}, 404
    def updateUser(self, user_id):
        
    