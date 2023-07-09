
from webapp import app
from flask_sqlalchemy import SQLAlchemy
from os import path

DB_NAME = "database.db"
app.secret_key = "127-924-831"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)


if not path.exists('webapp/'+DB_NAME):
        db.create_all(app=app)
        print('created database')

 


     

