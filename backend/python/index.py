from client import get_client

es = get_client()

def create_index():
    try:
        if es.indices.exists(index='my_index'):
            print('Index already exists.')
        else:
            es.indices.create(
                index = 'my_index',
                settings = {
                    'index': {
                        "number_of_shards": 2,  
                        "number_of_replicas": 1
                    }
                }
            )
    except Exception as e:
        print(f'Error: {e}')
        exit(1)

def delete_index():
    try: 
        if es.indices.exists(index='my_index'):
            es.indices.delete(index='my_index')
            print('Index deleted.')
        else:
            print('Index does not exist.')
    except Exception as e:
        print(f'Error: {e}')
        exit(1)