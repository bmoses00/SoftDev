# Brian Moses
# SoftDev1 pd 2
# K#10: Jinja tuning
# 2019-9-22

from flask import Flask, render_template
import csv
import random


OCCUPATIONS = {}
occupations = []
PERCENTAGES = []
mylist = zip(occupations, PERCENTAGES)

with open('static/occupations.csv') as csv_file:  #open CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')  #instantiate CSV reader object
    line_count = 0  #make sure header isn't included in dictionary
    for row in csv_reader:  #populate dictionary with keys and values
        if(line_count == 0):
            line_count += 1
        else:
            OCCUPATIONS[row[0]] = float(row[1])
    OCCUPATIONS.pop("Total")

for x, y in OCCUPATIONS.items():
    PERCENTAGES.append(str(y) + "%")
    occupations.append(x)

def selector():  #function to randomly select an occupation
    randomValue = random.random() * 99.8
    threshold = 0
    for x, y in OCCUPATIONS.items():
        if(randomValue < (threshold + y)):
            return x
        else:
            threshold += y


app = Flask(__name__)

@app.route('/')
def hello_world():
    return selector()

@app.route("/my_foist_template")
def foist():
    return ("Your future occupation is: " + selector() + render_template("my_foist_template.html",
                           collection = mylist))

if __name__ == "__main__":
        app.debug = True
        app.run()
