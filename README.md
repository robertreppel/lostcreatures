#Elasticsearch With Vancouver Animals, Lost & Found

##Getting Started:

1. Install https://www.docker.com/ and  https://www.getpostman.com/.

3. 'docker-compose up -d'

4. Verify Elasticsearch is up: http://localhost:9200/

4. 'docker exec lostcreatures_elastic_1 python /scripts/download-lostanimals.py'

5. Check if 'animals' index exists: http://localhost:9200/_cat/indices?v  

6. Try a freetext search: 'http://localhost:9200/animals/_search?q=toby'

7. In Chrome, start Postman and and import 'ElasticsearchQueryExamples.json.postman_collection'.

8. Try some queries.

##HowTo:

- Elasticsearch cheat sheet: http://lzone.de/cheat-sheet/ElasticSearch

- https://www.elastic.co/guide/en/elasticsearch/reference/2.0/_executing_searches.html
