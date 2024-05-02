
from .app import app
from flask_marshmallow import Marshmallow
from .models import User
from .models import Admin
from .models import Ticket
from flask_marshmallow import fields

marshmallow  =Marshmallow(app)

class UserSchema(marshmallow.SQLAlchemySchema):
    class Meta():
        model  = User
        load_instance = True
        fields = ("user_id", "fname", "lname", "email", "phone_num")
user_schema = UserSchema()
users_schema  = UserSchema(many=True)

class AdminSchema(marshmallow.Schema):
    class Meta():
        fields = ("emp_id", "fname", "lname", "email", "phone_num", "dept")
        model  = Admin
admin_schema = AdminSchema()
admins_schema  = AdminSchema(many=True)


class TicketSchema(marshmallow.Schema):
    class Meta():
        fields = ("ticket_id", "title", "body", "raised_by", "assigned_to", "created_at")
        model  = Ticket
ticket_schema = TicketSchema()
tickets_schema  = TicketSchema(many=True)

