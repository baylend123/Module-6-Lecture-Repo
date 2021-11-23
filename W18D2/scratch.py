'''
Psycopg2:
    # Fetching one record
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute(
            """
            SELECT *
            FROM widgets
            """)
        results = curs.fetchone()
        print(results)
FLask:

WTForms:


'''
# import psycopg2
# CONNECTION_PARAMETERS = {
#     "dbname": "book_app",
#     "user": "book_app_user",
#     "password": "password",
# }

# with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#     with conn.cursor() as curs:
#         curs.execute(
#             '''
#             CREATE TABLE books (
#             id SERIAL PRIMARY KEY,
#             title VARCHAR(50),
#             author VARCHAR(50),
#             rating VARCHAR(50)
#             );
#             '''
#         )

# def add_widget(shape, color):
#             curs.execute(
#                 '''
#                 INSERT INTO books (author, title, rating)
#                 VALUES (%(color)s, %(shape)s)
#                 ''',
#                 {
#                     'author' : author,
#                     'title': title,
                    # 'rating' : rating
                    
#                 }
#             )

'''
# Fetching one record
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        curs.execute(
            """
            SELECT *
            FROM books
            """)
        results = curs.fetchall()
        print(results)
'''