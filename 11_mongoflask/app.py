# Brian Moses
# SoftDev1 pd 2
# K11: mongoflask
# 2020-03-05

from pymongo import MongoClient
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")

@app.route('/gross_results')
def gross():
    client = MongoClient() # sets to localhost automatically
    db = client.MosDB
    col = db.movies
    print (request.args['gross'])
    return render_template("index.html", gross = [movie_data["Title"] for movie_data in col.find({"US_Gross": {"$gt": gross}})]) #add results

if __name__ == "__main__":
        app.debug = True
        app.run()
