from pymongo import MongoClient
client = MongoClient() # sets to localhost automatically
db = client.database_1

collection = db.collection_1

dict_list = [{
    "mango": 5,
    "pineappe": 23,
    "tomato": 4
}]

result = collection.insert_many(dict_list)

print(collection.find_one({"mango": 5}))
print(result)
print(db.list_collection_names())
