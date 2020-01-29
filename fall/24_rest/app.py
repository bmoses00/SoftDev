from flask import Flask, render_template
import urllib, json

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def root():
    link = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=100&api_key=W56Oyc2HC3Kpl9qXvqmkIawDe3MeQbaFe053pgJF"
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)
    return render_template("index.html",
                            pic = data["photos"][0]["img_src"])

if __name__ == "__main__":
    app.debug = True
app.run()
