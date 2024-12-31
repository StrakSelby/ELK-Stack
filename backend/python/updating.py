from pprint import pprint
import client, inserting

es = client.get_client()

def update_existing_field():
        for doc_id in inserting.document_ids:
                response = es.update(
                        index='my_index',
                        id=doc_id,
                        script={
                        "source": "ctx._source.title = params.title",  
                        "params": {
                                "title": "Old title"
                        }
                },
                )
                pprint(response) 