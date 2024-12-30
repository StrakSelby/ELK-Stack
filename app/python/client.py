from elasticsearch import Elasticsearch
from pprint import pprint

def get_client():
    es = Elasticsearch('http://localhost:9200')
    client_info = es.info()
    print('Connected to Elasticsearch!\n')
    pprint(client_info.body)
    return es 


    

   