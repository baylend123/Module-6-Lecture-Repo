from flask import Flask, render_template 
from app.config import Config
from app.routes.book_routes import book_router




app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(book_router, url_prefix='/api/books')


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/books')
def books():
    books=["harry potter","LOTR","The giver"]
    return render_template('books.html', books=books)