from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from bson.objectid import ObjectId
import json
from .models import *

# remove ObjectID in result query
def parse_json(cursor):
    data = []
    for doc in cursor:
        doc['_id'] = str(doc['_id']) # This does the trick!
        data.append(doc)
    return data

# call product collection from mongo client
product_col = db['products']


# Get product dashboard
def index(request):
    temp = loader.get_template('product_index.html')
    query = product_col.find()
    contex = {'products':parse_json(query)} # {}, {'_id': False}
    print(type(contex),'\n',contex,'\n ><><><><><><><><><><><><><><><><')

    return HttpResponse(temp.render({contex, request})) #JsonResponse(contex)

# Post new product information
def new_product(request):
    template = loader.get_template('add_product.html')
    return HttpResponse(template.render({}, request))
# Save pdroduct info to database
def add_product(request):
    product_dict = {
        'name' : request.POST['productNameInput'],
        'brand' : request.POST['brandInput'],
        'warranty' : request.POST['warrantyInput'],
        'images' : request.POST['imagesInput'],
        'price' : request.POST['priceInput'],
        'catalog' :request.POST['catalogInput'],
        'stock' : request.POST['stockInput'],
        'description' : request.POST['descriptionInput'],
    }
    product_col.insert_one(product_dict)
    for x in product_col.find():
        print(x['name'])
    return HttpResponseRedirect(reverse('products'))


def delete(request,_id):
    product_col.delete_one({'_id':ObjectId(_id)})
    print(f'delete product {_id} completed!')
    return HttpResponseRedirect(reverse('products'))









res = {}
for i in range(5):
    product_dict = {
        'name' : 'name '+str(i+1),
        'brand' : 'brand '+str(i+1),
        'warranty' : 'warranty '+str(i+1),
        'images' : 'image '+str(i+1),
        'price' : 'price '+str(i+1),
        'catalog' :'catalog '+str(i+1),
        'stock' : 'stock '+str(i+1),
        'description' : 'descrip '+str(i+1),
    }
    res.update(product_dict)
contex2 = {'products':res}

