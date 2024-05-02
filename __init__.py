from app import app
from models import db


def initDB():
    app.app_context().push()
    db.create_all()
    
    



if __name__ == '__main__':
  initDB() 
  app.run(debug=True)