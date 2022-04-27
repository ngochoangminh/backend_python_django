import sys
sys.path.append('.')
from pymongo.errors import CollectionInvalid
from collections import OrderedDict
from backend_mongo.py_mongodb import get_db

db = get_db()
collection = 'products'
products_schema ={
    'name': {
        'type': 'string',
        'required': True,
    },
    'brand':{
        'type':'string',
        "nullable": True,
    },
    'catalog':{
        'type':'string',
        "nullable": True,
    },
    'images':{
        'type':'text',
        "nullable": True,
    },
    'stock':{
        'type': 'int',
        'required': True,  
    },
    'price':{
        'type': 'int',
        'required': True,
    },
    'warranty':{
        'type':'date',
        'required': True,
    },
    'description':{
        'type':'text',
        "nullable": True,
    }
}

validator = {
                '$jsonSchema': {
                    'bsonType': 'object', 
                    'properties': {}
                    }    
            }
required = []

for field_key in products_schema:
    field = products_schema[field_key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')

    if type(minimum) == int:
        properties['minimum'] = minimum

    if field.get('required') is True: required.append(field_key)

    validator['$jsonSchema']['properties'][field_key] = properties

if len(required) > 0:
    validator['$jsonSchema']['required'] = required

query = [('collMod', collection), ('validator', validator)]

# try:
#     db.create_collection(collection)
# except CollectionInvalid:
#     pass

# command_result = db.command(OrderedDict(query))
