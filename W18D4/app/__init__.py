try:
    from flask import Flask
    from flask_migrate import Migrate
    from app.models import Book, db
    import os
except ImportError as err:
    print('**************', err)
    

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLAlchemy_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app,db)

@app.route('/')
def index():
    book = Book.query.get(1)
    return book.to_dict()
