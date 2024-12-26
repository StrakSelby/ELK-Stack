## Elasticsearch methods
### Get nodes status
```
GET _nodes/stats
```
### Get cluster health
```
GET _cluster/health
```
### PUT
```
PUT name_of_the_index/_doc/_id
{
        "field": "value",
        "field": "value"
}
```
### POST (auto generated id)
```
POST name_of_the_index/_doc/
{
        "field": "value",
        "field": "value"
}
```
### GET
```
GET name_of_the_index/_doc/_id
```
### Create END point (not overide the document)
```
PUT name_of_the_index/_create/_id
{
        "field": "value",
        "field": "value"
}
```
### Update the document
```
POST name_of_the_index/_update/_id
{
        "doc":{
                "field": "value"
        }
}
```
### Delete the document
```
DELETE name_of_the_index/_doc/_id
```
### Retrieve all document from an index
```
GET name_of_the_index/_search
```
### Get the extact total number of hits
```
GET name_of_the_index/_search
{
        "track_total_hits": true
}
```
### Search for value within a specific time range
```
GET name_of_the_index/_search
{
        "query": {
                "Specify the type of query" {
                        "field": {
                                "gte": "lowest value"
                                "lte": "highest value"
                        }
                }
        }
}
```
### Aggregation (summarizes value as metrics, statistics...etc)
```
GET name_of_the_index/_search
{
        "aggs": {
                "name of the aggregation": {
                        "Specify the type of aggregation": {
                                "field": "name of the field to aggreate"
                                "size": how many buckets
                        }
                }
        }
}
```
### Combine query and aggregation
```
GET name_of_the_index/_search
{
        "query": {
                "match": {
                        "field": "value"
                },
                "aggregations": {
                        "name of the aggregation": {
                             "significant_text": {"field": "value"}   
                        }
                }
        }
}
```
### Recall
```
GET name_of_the_index/_search {
        "query": {
                "match":{
                        "Specify the field to search": {
                                "query": "Enter search terms"
                        }
                }
        }
}
```
### Recall with AND operator
```
GET name_of_the_index/_search {
        "query": {
                "match":{
                        "Specify the field to search": {
                                "query": "Enter search terms",
                                "operator": "and"
                        }
                }
        }
}
```
### minimum_should_match
```
GET name_of_the_index/_search {
        "query": {
                "match":{
                        "Specify the field to search": {
                                "query": "Enter search terms",
                                "minimum_should_match": Enter number of field to match
                        }
                }
        }
}
```