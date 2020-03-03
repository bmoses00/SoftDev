from pymongo import MongoClient
import json

client = MongoClient() # sets to localhost automatically
db = client.MosDB
col = db.movies

with open('movies.json') as json_file:
    movies_string = json_file.read()
    movies_list = json.loads(movies_string)
    col.insert_many(movies_list)
