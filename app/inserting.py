import json
from client import get_client

def insert_document():
    es = get_client()
    dummy_data = json.load(open('dummy_data.json'))
    def insert_document(document):
        response = es.index(index='my_index', body=document)
        return response
    def print_info(response):
        print(f"""Document ID: {response['_id']} is '{
            response["result"]}' and is split into {response['_shards']['total']} shards.""")      

    print('\nInserting documents...\n')
    for document in dummy_data:
        response = insert_document(document)
        print_info(response)