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
PUT favorite_candy/_doc/1
{
        "fistname": "John",
        "candy": "Lolipop"
}
```
### POST (auto generated id)
```
POST favorite_candy/_doc/
{
        "fistname": "Joe",
        "candy": "Milo"
}
```
### GET
```
GET favorite_candy/_doc/1
```
### Create END point (not overide the document)
```
PUT favorite_candy/_create/1
{
        "fistname": "John",
        "candy": "Lolipop"
}
```
### Update the document
```
POST favorite_candy/_update/1
{
        "doc":{
                "candy": "M&M"
        }
}
```
### Delete the document
```
DELETE favorite_candy/_doc/1
```