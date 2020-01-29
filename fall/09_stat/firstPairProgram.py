from flask import Flask
app = Flask(__name__) #create new instance of flask
@app.route("/")
def hello_world():
    return "No"

coll = [0, 1]

if __name__ == "__main__":
    app.debug = True
    app.run()
