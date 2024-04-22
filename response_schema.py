from .app import app
from flask_marshmallow import Marshmallow
from .models import User
from .models import Admin
from .models import Ticket

marshmallow  =Marshmallow(app)

class UserSchema(marshmallow.Schema):
    class UserInfo:
        fields = ("user_id", "fname", "lname", "email", "phone_num")
        model  = User
user_schema = UserSchema()
users_schema  = UserSchema(many=True)

class AdminSchema(marshmallow.Schema):
    class AdminInfo:
        fields = ("emp_id", "fname", "lname", "email", "phone_num", "dept")
        model  = Admin
admin_schema = AdminSchema()
admins_schema  = AdminSchema(many=True)


class TicketSchema(marshmallow.Schema):
    class TicketInfo:
        fields = ("tikcet_id", "title", "body", "raised_by", "assigned_to", "created_at")
        model  = Ticket
ticket_schema = TicketSchema()
tickets_schema  = TicketSchema(many=True)

