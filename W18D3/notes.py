'''
Steps for setting up Flask-SQLAlchemy
    Create your database & user in psql.
        create user book_user with password 'password';
        create database book_database with owner 'book_user';
    Add a DATABASE_URL to your .env
        DATABASE_URL=postgresql://book_user:password@localhost/book_database


    Install psycopg2, sqlalchemy, and flask-sqlalchemy
        pipenv install psycopg2-binary sqlalchemy flask-sqlalchemy

Flask sessions
    Sessions let you store user-specific information on a cookie.

    You must have a secret key (SECRET_KEY) set on your application to use the session object.

'''

