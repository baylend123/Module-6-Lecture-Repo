from flask import Blueprint, request
from flask.templating import render_template
from app.forms import BookForm

book_router = Blueprint('books', __name__)

ALL_BOOKS = [{
    'title' : 'Harry potter',
    'author' : 'JK',
    'rating' : 'good book'
},{
    'title' : 'Harry potter',
    'author' : 'JK',
    'rating' : 'good book'
},{
    'title' : 'Harry potter',
    'author' : 'JK',
    'rating' : 'good book'
},]


@book_router.route('/all')
def all_books():
    return "My all books page"


@book_router.route('/new_book', methods=['GET', 'POST'])
def add_book():
    # print(request.json)
    form = BookForm()

    if form.validate_on_submit():
        print("form data ----",  form.data)
        new_book = {
            'title': form.data['title'],
            'author': form.data['author'],
            'rating': form.data['rating'],
        }
        ALL_BOOKS.append(new_book)
        return render_template('all_books.html', books=ALL_BOOKS)
    else:
        print(form.errors)
        return render_template('add_book.html', form=form)