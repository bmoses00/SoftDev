from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/") 
def root():
    link = "http://api.citybik.es/v2/networks"
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    data = data["networks"][0]
    return render_template("index.html",
                            info = data["location"]["city"],
                            name = data["id"])

if __name__ == "__main__":
    app.debug = True
app.run()
