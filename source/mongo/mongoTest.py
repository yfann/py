from pymongo import MongoClient
import datetime

class MongoStore(object):
    def __init__(self,connectionStr):
        self.client=MongoClient(connectionStr)
        self.db=self.client['PyMongoDB']
        self.collection=self.db['test']
    
    def insert(self,obj):
        return self.collection.insert_one(obj).inserted_id

    def insert_all(self,objs):
        result=self.collection.insert_many(objs)
        return result.inserted_ids

store=MongoStore('mongodb://super:super@localhost:27017/')

testData={
    "name":"yfann",
    "desc":"芝士就是力量",
    "favor":["mongodb","python","c#"],
    "createTime":datetime.datetime.utcnow()
}

store.insert(testData)