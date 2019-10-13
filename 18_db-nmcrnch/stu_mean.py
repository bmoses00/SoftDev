# Mohidul Abedin; Brian Moses; Team Mo^2
# SoftDev1 pd2
# K17 -- No Trouble
# 2019-10-11
import sqlite3
import csv

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #opens the file MUST RUN db_builder first
c = db.cursor()

def put_data_in(file_path: str, table_name):
    """
    Reads a csv file with three columns and enters into a table. Table must exist already

    :param file_path: Path to csv file to enter data in. The csv should only have 3 columns
    :param table_name: Name of table
    """
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            values = list(row.values())
            db.execute("INSERT INTO {} VALUES ('{}', {}, {});".format(table_name, *values))

averages = [] # 2d list containing name, id, average
def computeAverages():
    # gathers data about name, id, class, and class grade from db
    command = "SELECT name, students.id, code, mark FROM students, courses WHERE students.id = courses.id;"
    studentData = list(c.execute(command)) # converts into a list from cursor object

    # the code is executed for the 1st student
    currentStudent = studentData[0][0]
    sum = studentData[0][3]
    countGrades = 1
    counter = 1

    while (counter < len(studentData)):
        # if we have iterated past the grades for one student
        if currentStudent != studentData[counter][0]:
            averages.append([studentData[counter-1][0], studentData[counter-1][1], sum / countGrades])
            sum = 0
            countGrades = 0
            currentStudent = studentData[counter][0]
        # this tallies the sum and number of grades, for average later
        countGrades += 1
        sum += studentData[counter][3]
        counter += 1

    # for the last student
    averages.append([studentData[counter-1][0], studentData[counter-1][1], sum / countGrades])

def createStuAvg():
    c.execute("CREATE TABLE IF NOT EXISTS stu_avg (id INTEGER PRIMARY KEY, average INTEGER);")
    for keys in averages:
        c.execute("INSERT INTO stu_avg VALUES (" + str(keys[1]) + ", " + str(keys[2]) + ");")

def searchForStudent(input):
    if input == "":
        print (averages)
    else:
        for classData in studentData:
            if input == classData[0] or int(input) == classData[1]:
                print (classData)

def writeToCsv():
    with open("data/courses.csv", "a") as courses:
        courses.write("ceramics,55,11\n")
        courses.write("greatbooks,92,12\n")
        courses.write("softdev,45,13\n")
        courses.write("physics,100,14\n")
        courses.write("systems,5,16\n")
        courses.write("calculus,2,15\n")
    with open("data/students.csv", "a") as students:
        students.write("Bob,45,11\n")
        students.write("Bill,49,12\n")
        students.write("Billiam,84,13\n")
        students.write("Bo,153,14\n")
        students.write("Boses,354,16\n")
        students.write("Byler,9001,15\n")

writeToCsv()
db.execute("CREATE TABLE IF NOT EXISTS students (name STRING, age INTERGER, id INTERGER PRIMARY KEY);")
put_data_in("./data/students.csv", "students")
db.execute("CREATE TABLE IF NOT EXISTS courses (code STRING, mark INTERGER, id INTERGER);")
put_data_in("./data/courses.csv", "courses")
computeAverages()
createStuAvg()
print("Input name or id (case sensitive). Input nothing to see all students' average")
searchForStudent(input())

db.commit()
db.close()
