import pymongo

serverSelectionTimeoutMS=5000
MONGODB_CLOUD = 'mongodb+srv://ngochm:ohio2022@cluster0.xf35l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'



def get_db(info=MONGODB_CLOUD, timeouts=serverSelectionTimeoutMS):
    return pymongo.MongoClient(info, timeouts)


if __name__ == '__main__':
    try: 
        dbclient = get_db(MONGODB_CLOUD)
        print(dbclient.server_info())

        print('\t',dbclient.list_collection_names())
    except:
        print('Mongodb connect False')