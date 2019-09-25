from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return "h"

@app.route('/auth')
def auth():
    print(app)
    print(request)
    print(request.args)
    return "apple"

@app.route('/index.html')
def hello_world():
    print(app)
    print(request)
    print(request.args)
    return render_template("index.html")

if __name__ == "__main__":
        app.debug = True
        app.run()
