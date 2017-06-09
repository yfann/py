from pymongo import MongoClient

class MongoStore(object):
    def __init__(self,connectionStr):
        self.client=MongoClient(connectionStr)
        self.db=self.client['blog']
        self.collection=self.db['articles']
    
    def insert(self,obj):
        return self.collection.insert_one(obj).inserted_id

    def insert_all(self,objs):
        result=self.collection.insert_many(objs)
        return result.inserted_ids