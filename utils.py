from .models import User
from .models import Admin
from .models import Ticket
from .models import db
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from faker import Faker


faker  = Faker('en-IN')


def populateDB():
    for _ in range(100):
        user= User(
            fname= faker.first_name(),
            lname = faker.last_name(),
            email= faker.email(),
            phone_num = faker.phone_number()
        )
        db.session.add(user)

        admin = Admin(
            fname= faker.first_name(),
            lname = faker.last_name(),
            email= faker.email(),
            phone_num = faker.phone_number(),
            dept = faker.word()
        )
        db.session.add(admin)
        
        ticket = Ticket(
            title=faker.sentence(nb_words=5),
    body=faker.paragraph(nb_sentences=3),
    raised_by=faker.random_int(0,100),  
    assigned_to=faker.random_int(0,100),  
    created_at=faker.date_time()
        )
        db.session.add(ticket)

    db.session.commit()
