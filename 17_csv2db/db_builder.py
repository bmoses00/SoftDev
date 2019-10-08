#Brian Moses
#SoftDev pd 2
#K17 :: No Trouble
#Oct 7, 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

# test SQL stmt in sqlite3 shell, save as string
command = """

CREATE TABLE table (name TEXT PRIMARY KEY, id INTEGER);
INSERT INTO table ("Bob", 284192048);


"""

c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
