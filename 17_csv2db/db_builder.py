#Brian Moses
#SoftDev pd 2
#K17 :: No Trouble
#Oct 7, 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(row["name"])

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

# test SQL stmt in sqlite3 shell, save as string

command = "CREATE TABLE students (name TEXT PRIMARY KEY, id INTEGER);"
c.execute(command)
command = "INSERT INTO students VALUES ('Bob', 2531);"
c.execute(command)
command = "SELECT * FROM students;"
c.execute(command)
print(c.fetchall())




#==========================================================

db.commit() #save changes
db.close()  #close database
