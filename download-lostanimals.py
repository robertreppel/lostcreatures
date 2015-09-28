
# Import Vancouver's lost animals into Elasticsearch

import urllib
import json
from pprint import pprint
from datetime import datetime
from elasticsearch import Elasticsearch

vancouverLostAnimalsFtp = 'ftp://webftp.vancouver.ca/OpenData/json/LostAnimals.json'
print "Importing Vancouver lost & found animals from " + vancouverLostAnimalsFtp

lostAnimalsJson = urllib.urlopen(vancouverLostAnimalsFtp)
lostAnimalsJsonArray = json.load(lostAnimalsJson)
es = Elasticsearch("http://localhost")

animalCount = 0
for i in lostAnimalsJsonArray:
    animalCount = animalCount + 1
    res = es.index(index="animals", id=str(animalCount), doc_type="lost", body=i)
print

print "Imported " + str(animalCount)
