ENCODING = "utf-8"
import json
from urllib.request import urlopen

class data():
    def __init__(self):
        pass
    def getdata(self):
        url = "https://www.velo-antwerpen.be/availability_map/getJsonObject"
        response = urlopen(url)
        data_json = json.loads(response.read())
        with open("data.json","w",encoding = ENCODING) as f:
            json.dump(data_json,f)
    def printdata(self):
        with open("data.json","r",encoding = ENCODING) as f:
            print(f.read())
    def opendata(self):
        with open("data.json","r",encoding = ENCODING) as f:
            return f.read()