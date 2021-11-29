from flask import Flask
import sqlalchemy
from app.models import Publisher, db, Book, Author, publishers_books
from app.routes.author_routes import author_bp
from app.routes.book_routes import book_bp
from app.routes.session_routes import session_bp
from flask_migrate import Migrate
from app.config import Config

app = Flask(__name__)
# add your configuration
app.config.from_object(Config)
# hook your db to the app
db.init_app(app)
# set up the ability to migrate
migrate = Migrate(app, db)

app.register_blueprint(author_bp, url_prefix='/authors')
app.register_blueprint(book_bp, url_prefix='/books')
app.register_blueprint(session_bp, url_prefix='/session')


#spin up the app and hit this route to seed your db
@app.route('/seeder')
def seed_route():
    try: 
        author = Author(name='Jk Rowling')
        publisher = Publisher(name='Europe')
        publisher2 = Publisher(name='USA')
        db.session.add(publisher)
        db.session.add(publisher2)
        db.session.add(author)
        db.session.commit()
        new_book = Book(title='Harry Potter and the Goblet Of Fire',
                        pages=636,
                        author_id=author.id
                        )
        new_book2 = Book(title='Harry Potter and the Half Blood Prince',
                        pages=636,
                        author_id=author.id
                        )
        # staging the session with all of the new instances you want to add
        db.session.add(new_book)
        db.session.add(new_book2)
        # commit the changes to the db
        db.session.commit()
        publisher_book1 = publishers_books.insert().values(book_id=1, publisher_id=1)
        publisher_book2 = publishers_books.insert().values(book_id=2, publisher_id=1)
        publisher_book3 = publishers_books.insert().values(book_id=1, publisher_id=2)

        db.session.execute(publisher_book1)
        db.session.execute(publisher_book2)
        db.session.execute(publisher_book3)
        db.session.commit()
        return {'hey' : 'you did it'}
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        return {'Error' : f'{e}'
        }


@app.route('/seeder_undo')
def seed_undo():
    # get all the books in the db
    books = Book.query.all()
    #loop and delete each one
    [db.session.delete(book) for book in books]
    #get all the authors
    authors = Author.query.all()
    # loop and delete
    [db.session.delete(author) for author in authors]

    publishers = Publisher.query.all()
    [db.session.delete(publisher) for publisher in publishers]
    # resetting the id counter on both tables
    db.session.execute('''
    TRUNCATE TABLE books RESTART IDENTITY CASCADE
    ''')
    db.session.execute('''
    TRUNCATE TABLE authors RESTART IDENTITY CASCADE
    ''')
    
    db.session.execute('''
    TRUNCATE TABLE publishers RESTART IDENTITY CASCADE
    ''')
    
    
    db.session.commit()
    # commit the session

    return {'db' : 'unseeded'}