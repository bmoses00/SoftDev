# Brian Moses
# SoftDev1 pd 2
# K#08: Lemme Flask You Sump’n
# 2019-9-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("index.html")


if __name__ == "__main__":
        app.debug = True
        app.run()
