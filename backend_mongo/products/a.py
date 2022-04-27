
import mongoengine
cluster = "mongodb+srv://ngochm:ohio2022@cluster0.xf35l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
def gedb_mongoengine():
    return mongoengine.connect(cluster)

if __name__ == '__main__':
    try: 
        dbclient = gedb_mongoengine()
        print(dbclient.server_info())
        print('\t',dbclient.list_collection_names())
    except:
        print(F'Mongodb connect False')