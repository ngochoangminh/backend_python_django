import pymongo
import sys
# sys.path.append('.')
# print(sys.path)
# from config import mongo_user, mongo_password, atlas_cluster, db_name

mongo_user = 'ngochm'
mongo_password = 'ohio2022'
atlas_cluster = 'cluster0.xf35l.mongodb'
db_name = 'myFirstDatabase'
serverSelectionTimeoutMS=5000


cluster = f'mongodb+srv://{mongo_user}:{mongo_password}@{atlas_cluster}.net/{db_name}?retryWrites=true&w=majority'
def get_db():
    client = pymongo.MongoClient(cluster, 3000)
    return client[db_name]

if __name__ == '__main__':
   
    dbclient = get_db()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(dbclient.list_collection_names())
    print(type(dbclient['products'].find()))
    for x in list(dbclient['products'].find()):
        print(type(x))
