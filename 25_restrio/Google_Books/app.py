from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def root():
    link = "https://www.googleapis.com/books/v1/volumes/5iTebBW-w7QC"
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            description = data["volumeInfo"]["description"],
                            title = data["volumeInfo"]["title"],
                            author = data["volumeInfo"]["authors"][0],
                            id = data["id"])

if __name__ == "__main__":
    app.debug = True
app.run()
