from flask import Blueprint
import json 
from app.models import db, Book

book_bp = Blueprint('books', __name__)

@book_bp.route('/get_all_books')
def get_all_books():
    #get all books
    books = Book.query.all()
    return json.dumps({book.id : book.to_dict() for book in books})

@book_bp.route('/get_single_book')
def get_single_book():
    #this is usually a passed in value based on some user input
    id = 1
    book = Book.query.get(id)
    print(book.author.to_dict())
    return json.dumps(book.to_dict())
@book_bp.route('/start_with_h')
def starts_with_h():
    books = Book.query.filter(Book.title.like('H%'))
    # get the first book that matches
    # Book.query.filter(Book.title.like('H%')).first()
    return json.dumps({book.id : book.to_dict() for book in books})
@book_bp.route('/change_book_title')
def change_book_title():
    id = 1
    book = Book.query.get(id)
    book.title = 'Harry Potter and the Prisoner of Azkaban'
    return json.dumps(book.to_dict())
@book_bp.route('/delete_one_book')
def delete_one_book():
    book = Book.query.get(1)
    db.session.delete(book)
    db.session.commit()
@book_bp.route('/publishers')
def show_publishers():
    book = Book.query.get(1)
    print(book.publishers)
    return json.dumps([publisher.name for publisher in book.publishers])