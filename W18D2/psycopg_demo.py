import psycopg2

CONNECTION_PARAMETERS = {
    "dbname": "widget_database",
    "user": "widget_user",
    "password": "password",
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        # curs.execute(
        #     '''
        #     CREATE TABLE widgets (
        #     id SERIAL PRIMARY KEY,
        #     color VARCHAR(50),
        #     shape VARCHAR(50)
        #     );
        #     '''
        # )
        def add_widget(shape, color):
            curs.execute(
                '''
                INSERT INTO widgets (color, shape)
                VALUES (%(color)s, %(shape)s)
                ''',
                {
                    'color' : color,
                    'shape': shape
                }
            )
        add_widget("red", "square")
        add_widget("blue", "circle")
        add_widget("green", "rectangle")