import sqlite3
from data import data

conn = sqlite3.connect('velo.db')

c=conn.cursor()
address = []
bikes = []
id = []
lat = []
lon = []
name =[]
slots =[]
stationType = []
status =[]

c.execute("""CREATE TABLE IF NOT EXISTS velo (
            adress text,
            bikes integer,
            id integer,
            lat real,
            lon real,
            name text,
            slots integer,
            stationType text,
            status text
)""")

file = data().opendata()
for value in file:
    address.append(value['address'])
    bikes.append(value['bikes'])
    id.append(value['id'])
    lat.append(value['lat'])
    lon.append(value['lon'])
    name.append(value['name'])
    slots.append(value['slots'])
    stationType.append(value['stationType'])
    status.append(value['status'])

for number in range(len(id)):
    c.execute("INSERT INTO velo VALUES (:address, :bikes, :id, :lat, :lon, :name, :slots, :stationType, :status)",
    {'address':address[number],'bikes' : bikes[number],'id' : id[number],'lat' : lat[number],'lon' : lon[number],'name' : name[number],'slots' : slots[number],'stationType' : stationType[number],'status' : status[number]})
    conn.commit()

print(address[1])
conn.commit()

conn.close()