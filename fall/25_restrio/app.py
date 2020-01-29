# Brian Moses
# SoftDev pd2
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def root():
    link = "https://www.googleapis.com/books/v1/volumes/5iTebBW-w7QC"
    u = urllib.request.urlopen(link)
    response = u.read()
    book_data = json.loads(response)

    link = "http://api.citybik.es/v2/networks"
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    bike_data = data["networks"][0]

    link = "https://www.metaweather.com/api/location/2459115/"
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    weather_data = data["consolidated_weather"][0]

    return render_template("index.html",
                            description = book_data["volumeInfo"]["description"],
                            title = book_data["volumeInfo"]["title"],
                            author = book_data["volumeInfo"]["authors"][0],
                            id = book_data["id"],

                            info = bike_data["location"]["city"],
                            name = bike_data["id"],
                            company = bike_data["company"][0],

                            date = weather_data["applicable_date"],
                            weather = weather_data["weather_state_name"]
                            )

if __name__ == "__main__":
    app.debug = True
app.run()
