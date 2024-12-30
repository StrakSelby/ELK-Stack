from elasticsearch import Elasticsearch
from pprint import pprint

try:
    def get_client():
        # use to run locally
        es = Elasticsearch('http://localhost:9200')
        # es = Elasticsearch('http://es01:9200')
        # client_info = es.info()
        # print('Connected to Elasticsearch!\n')
        # pprint(client_info.body)
        return es 
except Exception as e:
    print(f'Error: {e}')
    exit(1)


    

   