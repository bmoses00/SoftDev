from pymongo import MongoClient

client = MongoClient() # sets to localhost automatically
db = client.restaurant_db

col = db.restaurants

def get_restaurants_in_borough(borough):
    return list(col.find({"borough": borough}))

def get_restaurants_in_zip(zip):
    return list(col.find({"address.zipcode": zip}))

def get_restaurants_by_zip_and_grade(zip, grade):
    return list(col.find({"address.zipcode": zip, "grades.0.grade": grade}))

def get_restaurants_by_zip_and_below_score(zip, score):
    return list(col.find({"grades.0.score": {"$lt": score}, "address.zipcode": zip}))

def get_high_quality_restaurants():
    return list(col.find(  { "grades.0.score": {"$ne": "C"}, "borough": {"$ne": "Staten Island"} }  ))

#print(get_restaurants_in_borough("Manhattan"))
#print(get_restaurants_in_zip("10301"))
#print(get_restaurants_by_zip_and_grade("11435", "A"))
#print(get_restaurants_by_zip_and_below_score("10036", 30))
#print(get_high_quality_restaurants())
