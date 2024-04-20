from app import app
from models import db
from utils import populateDB


def initDB():
    db.create_all()
    populateDB()



if __name__ == '__main__':
  initDB() 
  app.run(debug=True)