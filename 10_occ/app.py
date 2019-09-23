# Brian Moses
# SoftDev1 pd 2
# K#10: Jinja tuning
# 2019-9-22

from flask import Flask, render_template
import csv
import random

OCCUPATIONS = []
PERCENTAGES = []
mylist = zip(OCCUPATIONS, PERCENTAGES)

file = open("static/occupations.csv", "r") #opens file
workingList = file.readlines()[1:len(file.readlines())-1] # removes last, first elements of csv
for job in workingList:
    job = job.rsplit(",", 1)
    OCCUPATIONS.append(job[0])
    PERCENTAGES.append(float(job[1]))

file.close()


# select a value from 0 to 99.8
# this value is compared to the percentage of the occupation
# if the value is less than that percent, the job is returned
# else, threshold is increased by the percentage
# ------------------------------------------------------------------
# EX: randomValue = 12
# 12 < 6.1: FALSE
# threshold now = 0 + 6.1 = 6.1
# 12 < 6.1 + 5: FALSE (there was a 5% chance of this happening
#                      number being > 6.1 and < 11.1. This 5% is
#                      the percentage of this occupation)
# threshold now = 6.1 + 5 = 11.1
# 12 < 11.1 + 2.7: TRUE -> occupation is returned
def selector():
    randomValue = random.random() * 99.8
    threshold = 0

    while ()
    for (x, y) in mylist:
        print ("hi")
        if(randomValue < (threshold + y)):
            return x
        else:
            threshold += y


app = Flask(__name__)

@app.route('/')
def hello_world():
    return selector()

@app.route("/occupyflaskst")
def foist():
    return ("Your future occupation is: " + selector() + render_template("my_foist_template.html",
                           collection = mylist))

if __name__ == "__main__":
        app.debug = True
        app.run()
