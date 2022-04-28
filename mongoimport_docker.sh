docker exec -i mongodb sh -c 'mongoimport -u=root -p=root --authenticationDatabase admin -d DBLP -c publis --drop' < dblp.json
