#Launches and populates an Elasticsearch instance containing all lost animals in Vancouver.

##Getting Started:

1. 'docker run -d --name elasticsearch elasticsearch'   elasticsearch'

2. 'python download-lostanimals.py'

3. Verify that Elasticsearch has started and find the IP address (e.g. 172.17.0.1:9200): 'docker logs elasticsearch'

4. Check if 'animals' index exists: 'http://172.17.0.1:9200/_cat/indices?v'  

6. Freetext search: 'http://172.17.0.1:9200/animals/_search?q=toby'


##Howto

Elasticsearch cheat sheet: http://lzone.de/cheat-sheet/ElasticSearch
https://www.elastic.co/guide/en/elasticsearch/reference/2.0/_executing_searches.html


{"docs" : [ {"_id" : "AU_1PJ4xSSTQvIN1K10z", "_index" : "animals", "_type" : "lostanimal" },{ "_id" : "AU_1PLx0SSTQvIN1K2sB" }, "_index" : "animals", "_type" : "lostanimal" ] }


##Notes:

###Multi-Get

https://www.elastic.co/guide/en/elasticsearch/reference/1.4/docs-multi-get.html

curl http://172.17.0.1:9200/_mget -d '{
    "docs" : [
        {
            "_index" : "animals",
            "_type" : "lostanimal",
            "_id" : "AU_1PJ4xSSTQvIN1K10z"
        },
        {
            "_index" : "animals",
            "_type" : "lostanimal",
            "_id" : "AU_1PLx0SSTQvIN1K2sB"
        }
    ]
}'
