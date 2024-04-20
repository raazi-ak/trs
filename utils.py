from models import User
from models import Admin
from models import Ticket
from models import db
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from faker import Faker


faker  = Faker('en-IN')


def populateDB():
    for _ in range(100):
        user= User(
            user_id = faker.random_int(1,100),
            fname= faker.first_name(),
            lname = faker.last_name(),
            email= faker.email(),
            phone_num = faker.phone_number()
        )
        db.session.add(user)

        admin = Admin(
            emp_id = faker.random_int(1,50),
            fname= faker.first_name(),
            lname = faker.last_name(),
            email= faker.email(),
            phone_num = faker.phone_number(),
            dept = faker.word()
        )
        db.session.add(admin)
        
        ticket = Ticket(
            ticket_id = faker.random_int(),
            title=faker.sentence(nb_words=5),
    body=faker.paragraph(nb_sentences=3),
    raised_by=faker.random_int(1, 100),  
    assigned_to=faker.random_int(1, 50),  
    created_at=faker.datetime(timezone=True),
        )
        db.session.add(ticket)

    db.session.commit()
