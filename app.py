#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Manipulation de données avec MongoDB
"""

import pprint
from pymongo.mongo_client import MongoClient


client = MongoClient('mongodb://root:root@localhost:27017')
db = client.DBLP
publis = db.publis


nb_doc = db.publis.count_documents({})
print(f"Nombre de documents : {nb_doc}")
_ = input("Appuyez sur une touche pour continuer...")


print("\nLister tous les livres (type “Book”) :")
print(db.publis.find({ 'type': "Book" }))
books = db.publis.find({'type': "Book"})
for book in books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nLister les livres depuis 2014 :")
books = db.publis.find({'type': "Book", 'year': { "$gte": 2014 } })
for book in books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nLister les publications de l’auteur “Toru Ishida” :")
books = db.publis.find({ 'authors': {"$elemMatch": {"$eq": "Toru Ishida"}} })
for book in books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nLister tous les auteurs distincts :")
authors = db.publis.distinct('authors')
for author in authors:
    print(author)
_ = input("Appuyez sur une touche pour continuer...")


print("\nTrier les publications de “Toru Ishida” par titre de livre :")
books = db.publis.find({
    'type': "Book",
    'authors': { "$elemMatch": { "$eq": "Toru Ishida" } }
    }).sort('title', 1)
for book in books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nCompter le nombre de ses publications :")
nb_books = db.publis.count_documents({
    'authors': { "$elemMatch": { "$eq": "Toru Ishida" } }
    })
print(f"Nombre de publications : {nb_books}")
_ = input("Appuyez sur une touche pour continuer...")


print("\nCompter le nombre de publications depuis 2011 et par type :")
nb_books = db.publis.count_documents({'year': { "$gte": 2011 } })
print(f"Nombre de publications depuis 2011 : {nb_books}")
print("\nNombre de publications par type :")
nb_books = db.publis.aggregate([
    { '$group': { '_id': '$type', 'count': { '$sum': 1 } } }
])
for book in nb_books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nCompter le nombre de publications par auteur et trier le résultat par ordre croissant :")
books = db.publis.aggregate([
    { '$unwind': '$authors' },
    { '$group': { '_id': '$authors', 'nb_publis': { '$sum': 1 } } },
    { '$sort': { 'nb_publis': 1 } }
])
for book in books:
    pprint.pprint(book)

_ = input("Appuyez sur une touche pour continuer...")
