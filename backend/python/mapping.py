from pprint import pprint
from client import get_client

def create_mapping():
    es = get_client()
    mapping = {
        'properties': {
            'created_on': {'type': 'date'},
            'text': {
                'type': 'text',
                'fields': {
                    'keyword': {
                        'type': 'keyword',
                        'ignore_above': 256
                    }
                }
            },
            'title': {
                'type': 'text',
                'fields': {
                    'keyword': {
                        'type': 'keyword',
                        'ignore_above': 256
                    }
                }
            }
        }
    }
    es.indices.put_mapping(index='my_index', body=mapping)
    index_mapping = es.indices.get_mapping(index='my_index')
    # print('Created mapping:\n')
    # pprint(index_mapping["my_index"]["mappings"]["properties"])
