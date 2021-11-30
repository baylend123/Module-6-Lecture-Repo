try:
    from flask_sqlalchemy import SQLAlchemy
except ImportError as e:
    print('******************', e)

db = SQLAlchemy()

class Book(db.Model):
    __tabelname__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    '''
    Writing a to_dict() method
    We can make our code DRYer by adding a method to 
    our model classes to convert model instances to 
    dictionaries.

    That way we don’t have to rewrite the same code on 
    different routes when we send data to our front-end.
    '''
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
