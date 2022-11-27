import sqlite3

conn = sqlite3.connect('velo.db')

c=conn.cursor()

c.execute("""CREATE TABLE velo (
            adress text,
            bikes integer,
            id integer,
            lat real,
            lon real,
            name text,
            slots integer,
            status text
            )""")

conn.commit()

conn.close()