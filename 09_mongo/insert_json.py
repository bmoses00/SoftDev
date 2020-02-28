# Credits to William Cao for providing formatted JSON

from pymongo import MongoClient
import json

client = MongoClient() # sets to localhost automatically
db = client.restaurant_db

col = db.restaurants

with open('primer-dataset.json') as json_file:
    file_data_string = json_file.read()
    file_data_string = file_data_string.replace("$date", "date")
    restaurant_dict_list = json.loads(file_data_string)
    col.insert_many(restaurant_dict_list)

