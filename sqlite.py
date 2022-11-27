import sqlite3
from data import data

conn = sqlite3.connect('velo.db')

c=conn.cursor()
adress = []
bikes = []
id = []
lat = []
lon = []
name =[]
slots =[]
status =[]

c.execute("""CREATE TABLE IF NOT EXISTS velo (
            adress text,
            bikes integer,
            id integer,
            lat real,
            lon real,
            name text,
            slots integer,
            status text
)""")

file = data().opendata()
# for value in file:
#     adress.append(value['address'])
#     bikes.append(value['bikes'])
#     id.append(value['id'])
#     lat.append(value['lat'])
#     lon.append(value['lon'])
#     name.append(value['name'])
#     slots.append(value['slots'])
#     status.append(value['status'])

# for adress1 in adress:
#     print(adress)
print(file)

conn.commit()

conn.close()