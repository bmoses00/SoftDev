# Brian Moses
# SoftDev1 pd 2
# K#08: Lemme Flask You Sump’n
# 2019-9-10

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
