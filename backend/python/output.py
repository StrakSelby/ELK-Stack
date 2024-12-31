from pprint import pprint
from client import get_client

es = get_client()

def total_documents():
    print('Outputting all documents...\n')
    result = es.search(index='my_index', body={'query': {'match_all': {}}})
    print(f"Total documents: {result['hits']['total']['value']}\n")

def print_all_documents():
    print('\nPrinting each document...\n')
    result = es.search(index='my_index', body={'query': {'match_all': {}}})
    for document in result['hits']['hits']:
        for key, value in document['_source'].items():
            print(f"{key}: {value}", end=", ")
        print("\n")