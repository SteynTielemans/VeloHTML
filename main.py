import sqlalchemy as sa
from urllib.request import urlopen
import json

class json():
    def __init__():
        pass
    def getdata():
        url = "https://www.velo-antwerpen.be/availability_map/getJsonObject"
        response = urlopen(url)
        data_json = json.loads(response.read())