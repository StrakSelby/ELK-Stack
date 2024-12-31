import json
from tqdm import tqdm
from client import get_client

es = get_client()
document_ids = []

def insert_document():
    dummy_data = json.load(open('dummy_data.json'))
    for document in tqdm(dummy_data, total=len(dummy_data)):
        response = es.index(index='my_index', body=document)
        document_ids.append(response['_id'])


    # def insert_document(document):
    #     response = es.index(index='my_index', body=document)
    #     return response
    # def print_info(response):
    #     print(f"""Document ID: {response['_id']} is '{
    #         response["result"]}' and is split into {response['_shards']['total']} shards.""")      

    # print('\nInserting documents...\n')
    # for document in dummy_data:
    #     response = insert_document(document)
    #     print_info(response)