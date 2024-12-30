from pprint import pprint
from client import get_client

def output_documents():
    es = get_client()
    print('Outputting all documents...\n')
    result = es.search(index='my_index', body={'query': {'match_all': {}}})
    print(f"Total documents: {result['hits']['total']['value']}\n")

    print('\nPrinting each document...\n')
    for document in result['hits']['hits']:
        pprint(document['_source'])