from pymongo import MongoClient
import pprint


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
books = db.publis.find({ 'authors': { "$elemMatch": { "$eq": "Toru Ishida" } } })
for book in books:
    pprint.pprint(book)
_ = input("Appuyez sur une touche pour continuer...")


print("\nLister tous les auteurs distincts :")
authors = db.publis.distinct('authors')
for author in authors:
    print(author)
_ = input("Appuyez sur une touche pour continuer...")


print("\nTrier les publications de “Toru Ishida” par titre de livre :")
books = db.publis.find({'type': "Book", 'authors': { "$elemMatch": { "$eq": "Toru Ishida" } } }).sort('title', 1)
for book in books:
    pprint.pprint(book)
