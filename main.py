import pymongo
try:
    client=pymongo.MongoClient("mongodb+srv://pranav:pranav0510@cluster0.mgbscmu.mongodb.net/")
    print(mongodb_client.list_database_names())
    
except:
    mongodb_client.close()
    print('Connection is closed')