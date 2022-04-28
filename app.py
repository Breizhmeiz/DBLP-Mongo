from pymongo import MongoClient
import pprint


client = MongoClient('mongodb://root:root@localhost:27017')
db = client.DBLP
publis = db.publis
nb_doc = db.publis.count_documents({})
print(f"Nombre de documents : {nb_doc}")
