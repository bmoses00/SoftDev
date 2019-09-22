# Brian Moses
# SoftDev1 pd 2
# K #03: Know your fam
# 2019-9-10

import csv
import random

OCCUPATIONS = {}

with open('occupations.csv') as csv_file:  #open CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')  #instantiate CSV reader object
    line_count = 0  #make sure header isn't included in dictionary
    for row in csv_reader:  #populate dictionary with keys and values
        if(line_count == 0):
            line_count += 1
        else:
            OCCUPATIONS[row[0]] = float(row[1]);

def selector():  #function to randomly select an occupation
    randomValue = random.random() * 99.8
    threshold = 0
    for x, y in OCCUPATIONS.items():
        if(randomValue < (threshold + y)):
            return(x, y)
        else:
            threshold += y

print(selector())
