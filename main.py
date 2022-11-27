from urllib.request import urlopen
import json
ENCODING = "utf-8"

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

data().printdata()
