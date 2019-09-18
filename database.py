import sqlite3


class database:
    def __init__(self):
        try:
            conn = sqlite3.connect('test.db')
            curr = conn.cursor()
            query = '''CREATE TABLE "TEST_TABLE" (
                        "name"	TEXT NOT NULL UNIQUE,
                        "favourate_color"	TEXT,
                        "cat_or_dog"	TEXT
                        )'''
            curr.execute(query)
            conn.commit()
        except sqlite3.OperationalError:
            print('Table Created')

    def insert_data(self, name, favourate_color, cat_or_dog):
        try:
            conn = sqlite3.connect('test.db')
            curr = conn.cursor()
            query = '''INSERT INTO TEST_TABLE (name, favourate_color, cat_or_dog)
             VALUES ("{}", "{}","{}")'''.format(name, favourate_color, cat_or_dog)

            curr.execute(query)
            conn.commit()
        except sqlite3.IntegrityError:
            print('Row with this name already exists.')
