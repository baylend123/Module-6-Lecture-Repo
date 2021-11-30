'''
Setting Up Flask-Migrate
    Initialize your migrations repo.
flask db init
    Create a migration file.
flask db migrate
    Apply your migrations to your database.
flask db upgrade

Workflow
    When you make changes to your models:
    Run migrate to get a new migration script.
flask db migrate
    Run upgrade to apply the changes.
flask db upgrade    

Downgrading
Downgrading shouldn’t be a very common part of your
 workflow. If you want to downgrade a 
 migration, you can use the downgrade command.

To undo a single migration:

flask db downgrade
'''

'''
Model Instances vs. Dictionaries
Recall that, in JavaScript, we typically 
use objects for two purposes: as a collection 
of key/value pairs, and also as a collection of 
methods and properties.

In Python, key/value pairs in dictionaries 
are not the same as attributes on objects 
(a.k.a, classes).

book = Book.query.get(1)
print(book)
print(book.title)
If you try to send a model instance 
object from your server to your frontend, 
the frontend client won’t know what to do with it.

If we send a dictionary instead, 
Flask will automatically convert it to 
JSON so it can be understood by the client.
'''

'''
Returning JSON from Python
We need to convert our database objects 
into dictionaries so that we can use our 
Flask back-end as an API.

book = Book.query.get(1)
book_dict = {
    "id": book.id,
    "title": book.title,
}
print(book_dict)
'''