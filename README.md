---
created: 2022-04-28T14:30:08 (UTC +02:00)
tags: []
source: https://simplonline.co/briefs/8117a5b5-e07c-43f9-bcf5-a95724992345
author: Stephane Jamin-Normand
---

![](https://simplonline.co/_next/image?url=https%3A%2F%2Fsimplonline-v3-prod.s3.eu-west-3.amazonaws.com%2Fmedia%2Fimage%2Fjpg%2F4d22dd14-8988-41a9-bd16-5822893d1268.jpg&w=1280&q=75)

# Base de publications scientifiques

Il s’agit de créer une base Mongo, une collection, d’y insérer des données et de l’interroger grâce à Python.
Les documents fournis correspondent à un extrait d’une base de publications scientifiques, The DBLP Computer Science Bibliography.


## Contexte du projet

Le centre de recherche Breizhmeiz International souhaite un petit module d'accès simple aux publications scientifiques.
On vous demande de mettre en place une base de données MongoDB, orientée documents, pour gérer l'accès à ces publications.
De votre coté, vous allez tester les datas grâce à un petit script Python.


## Modalités pédagogiques

Le projet se fait seul et doit être rendu vendredi soir.

Vous allez suivre les étapes suivantes pour réaliser le projet :
- [X] Créer la base DBLP et y ajouter une collection publis,
- [X] importer dans la base les données du fichier dblp.json (Ca peut prendre un peu de temps),
- [X] écrire le script Python pour tester la base, exécuter le script et vérifier les résultats.


Le script Python doit permettre de :
- [X] Compter le nombre de documents de la collection publis;
- [X] Lister tous les livres (type “Book”) ;
- [X] Lister les livres depuis 2014 ;
- [X] Lister les publications de l’auteur “Toru Ishida” ;
- [X] Lister tous les auteurs distincts ;
- [X] Trier les publications de “Toru Ishida” par titre de livre ;
- [X] Compter le nombre de ses publications ;
- [X] Compter le nombre de publications depuis 2011 et par type ;
- [X] Compter le nombre de publications par auteur et trier le résultat par ordre croissant ;


Tous les affichages se font dans la console.

Et s'il vous reste du temps écrire un petit script qui :
- [X] demande le chemin d'un fichier json,
- [X] insére un ou plusieurs nouveaux documents, à partir de ce fichier, dans la collection publis.


Pour tester ce dernier script, créer un fichier json à partir des informations trouvées sur le site proposé en lien.

## Critères de performance

La connexion à MongoDB doit fonctionner et celle-ci doit contenir la collection publis avec l'ensemble des documents enregistrés.
Le code Python doit exécuter l'ensemble des requêtes demandées.

## Modalités d'évaluation

Présentation du code au formateur.

## Livrables

Un lien Github vers le code Python :
- `docker-compose up -d` / `docker-compose down` pour lancer la stack MongoDB
- `sh ./mongoimport_docker.sh dblp.json` pour remplir la base avec les données fournies
- `pip install -r requirements.txt` pour installer les dépendances
- `python3 app.py` pour lancer le script Python
- `sh ./mongoimport_docker.sh refs.json` pour ajouter les nouvelles références
