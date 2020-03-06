# Brian Moses
# SoftDev1 pd 2
# K11: mongoflask
# 2020-03-05

from pymongo import MongoClient
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
client = MongoClient() # sets to localhost automatically
db = client.MosDB
col = db.movies

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/gross_results')
def gross():
    lis = list(col.find({"US_Gross": {"$gt": int(request.args['gross'])}}))
    return render_template("index.html", gross = lis) #add results

@app.route('/ratings_results')
def ratings():
    lis = list(
                col.find({
                    "Rotten_Tomatoes_Rating": {"$gt": int(request.args['rotten_tomatoes'])},
                    "IMDB_Rating": {"$gt": int(request.args['imdb'])}
                })
            )
    return render_template("index.html", ratings = lis)

@app.route('/year_results')
def year():
    lis = [movie for movie in col.find({}) if int(movie["Release_Date"][-4:]) > int(request.args['year'])]
    return render_template("index.html", year = lis)

@app.route('/genre_results')
def genre():
    lis = [movie for movie in col.find({"Major_Genre": request.args['genre']})]
    return render_template("index.html", genre = lis)

if __name__ == "__main__":
        app.debug = True
        app.run()