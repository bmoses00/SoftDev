from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(__name__)
    return "No hablo queso"

@app.route('/cool')
def cool():
    return "You are cool"

@app.route('/pasta')
def food():
    return "Potato"

@app.route('/water')
def ocean():
    return "Fish"

if __name__ == "__main__":
        app.debug = True
        app.run()
