# Brian Moses
# SoftDev1 pd 2
# K#09: ’Tis Not a Race -- But You Will Go Faster
# 2019-9-22

from flask import Flask, render_template
app = Flask(__name__) #create new instance of flask
@app.route("/")
def hello_world():
    return "Yes"

coll = [0, 1, 1, 2, 3, 5, 8]

@app.route("/my_foist_template")
def foist():
    return render_template("my_foist_template.html",
                           collection = coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
