# Mohidul Abedin; William Cao; Team Mo Goes Cow
# SoftDev1 pd2
# K17 -- No Trouble
# 2019-10-10

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops






# print("----------------")
# print(foo)
# for bar in foo:
#     print (bar)

db.commit() #save changes
db.close()  #close database
