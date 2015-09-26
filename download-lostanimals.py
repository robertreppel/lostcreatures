
# Import all lost animals in Vancouver into Elasticsearch

import urllib
import json
from pprint import pprint
from datetime import datetime
from elasticsearch import Elasticsearch

# https://elasticsearch-py.readthedocs.org/en/master/

lostAnimalsJson = urllib.urlopen('ftp://webftp.vancouver.ca/OpenData/json/LostAnimals.json')
lostAnimalsJsonArray = json.load(lostAnimalsJson)

es = Elasticsearch("http://172.17.0.2")
animalCount = 0
for i in lostAnimalsJsonArray:
    print i["Name"]
    animalCount = animalCount + 1
    res = es.index(index="animals", doc_type="lost", body=i)
print animalCount
