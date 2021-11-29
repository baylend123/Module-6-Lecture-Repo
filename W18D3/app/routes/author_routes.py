from flask import Blueprint
import json 
from app.models import db, Author

author_bp = Blueprint('authors', __name__)

@author_bp.route('/get_all_authors')
def get_all_authors():
    #get all books
    authors = Author.query.all()
    return json.dumps({author.id : author.to_dict() for author in authors})

@author_bp.route('/get_single_author')
def get_single_author():
    #this is usually a passed in value based on some user input
    id = 1
    author = Author.query.get(id)
    print(author.books)
    return json.dumps(author.to_dict())
