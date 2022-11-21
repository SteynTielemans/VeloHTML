import sqlalchemy as sa
from urllib.request import urlopen
import json

class data():
    def __init__():
        pass
    def getdata():
        url = "https://www.velo-antwerpen.be/availability_map/getJsonObject"
        response = urlopen(url)
        data_json = json.loads(response.read())
        with open("data.json","w") as f:
            json.dump(data_json,f)

data.getdata()