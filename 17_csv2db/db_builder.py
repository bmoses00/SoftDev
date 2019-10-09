#Brian Moses
#SoftDev pd 2
#K17 :: No Trouble
#Oct 7, 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
# first table

# beginning and ending of each c.execute command
beginning = "INSERT INTO students VALUES ("
ending = ");"

command = "CREATE TABLE students (name TEXT PRIMARY KEY, age INTEGER, id INTEGER);"
c.execute(command)

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # add each row of the ordered dict to the db table
        command = beginning + "'" + row["name"] + "', " + row["age"] + ", " + row["id"] + ending
        c.execute(command)

# this code prints the table
# command = "SELECT * FROM students;"
# c.execute(command)
# print(c.fetchall())

#==========================================================
# second table
command =  "CREATE TABLE courses (code, mark INTEGER, id INTEGER);"
c.execute(command)

beginning = "INSERT INTO courses VALUES ("
ending = ");"

with open("courses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        command = beginning + "'" + row["code"] + "', " + row["mark"] + ", " + row["id"] + ending
        c.execute(command)

# command = "SELECT * FROM courses;"
# c.execute(command)
# print(c.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database
