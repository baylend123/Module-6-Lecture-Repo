from enum import unique
from operator import mod
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
Creating Models
    Models inherit from the db.Model class, which comes from our SQLAlchemy instance.

    If you want to specify a tablename, use the __tablename__ property.

Columns on models
    Columns are added to the model as class variables—instances of db.Column from our 
    SQLAlchemy instance.

    Column types (db.String, db.Integer, etc.) also come from our SQLAlchemy instance.

One-To-Many Relationships
    Let’s make a relationship between books and authors. 
    Each book belongs to one author, authors can have many books.

    First, let’s create the Author model.
One-To-Many Relationships
    Next we need to add a foreign key to the Book model that points to the Author model. 
        To make a column into a 
        foreign key we use db.ForeignKey(tablename.columnname).

        In a one-to-many relationship, the foreign key column will go on the child model 
        referencing the parent. The child is the “many” side of the relationship.
Adding the relationship property
    Add a db.relationship to both of the models.

    Use the back_populates property to connect the two relationship attributes.

    Use cascade="all, delete" on the parent model to cascade deletion of all 
    related child objects (https://docs.sqlalchemy.org/en/14/orm/cascades.html#delete).
    attribute_name = db.relationship("OtherModelName", back_populates="name_of_attribute_from_opposite_model")

'''
publishers_books = db.Table(
    'publishers_books',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('publisher_id', db.Integer, db.ForeignKey('publishers.id'), primary_key=True)
)

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    pages = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('Author', back_populates='books')
    publishers = db.relationship(
    "Publisher",
    secondary=publishers_books,
    back_populates="books"
)

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'pages' : self.pages,
            
            
        }

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    books = db.relationship('Book', back_populates='author', cascade='all, delete')

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'books' : [book.to_dict() for book in self.books]
        }

class Publisher(db.Model):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    books = db.relationship(
    "Book",
    secondary=publishers_books,
    back_populates="publishers"
)


