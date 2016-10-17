#Database

#-----------------------------------------
import sqlite3

db= sqlite3.connect('test.db')
db.commit()

#Create Table
# db.execute('CREATE TABLE student (name text, rank int)')
# db.commit()

#Insert Data

# db.execute('SELECT * FROM student ORDER BY rank)
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Jim',1))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('John',2))
# db.execute('INSERT INTO student (name,rank) values (?,?)',('Tim',3))
# db.commit()

#Read Data
# a = db.execute('SELECT * FROM student ORDER BY rank')
# print(a)
# #print(list(a))
# for i in list(a):
# 	print(i)

#Update Data

# db.execute('UPDATE student SET name=? WHERE rank=?',('Him',2))
# db.commit()

#Delete
# db.execute('DELETE FROM student WHERE rank = 2')
# db.commit()

#------------------------------------------
#Challenege
# import sqlite3

db= sqlite3.connect('example.db')
# #Create Table
# db.execute('CREATE TABLE subject (subjects text, students int, classes int)')
# db.commit()
# #Insert Data
# db.execute('INSERT INTO subject (subjects,students,classes) values (?,?,?)',('English',200,10))
# db.execute('INSERT INTO subject (subjects,students,classes) values (?,?,?)',('Chinese',50,8))
# db.execute('INSERT INTO subject (subjects,students,classes) values (?,?,?)',('Math',120,5))
# db.execute('INSERT INTO subject (subjects,students,classes) values (?,?,?)',('Science',90,11))
# db.commit()
# #Read Data
a = db.execute('SELECT * FROM subject ORDER BY students')
print(a)
print(list(a))
