import sqlite3

conn = sqlite3.connect('velo.db')

c=conn.cursor()



conn.commit()

conn.close()