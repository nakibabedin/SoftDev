#RICE EXPLOSION :: Nakib Abedin, Wilson Mach, Donald Bi
#SoftDev  
#k18:: SQLITE3 BASICS
#2022-10-25

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

c.execute("CREATE table courses (name TEXT, mark int, id int)")
with open("courses.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute(f"INSERT into courses values ({row['name']},{row['mark']},{row['id']})")


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


