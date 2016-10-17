#File IO

#open file
# f = open('example.txt','w')
# for i in range(10):
#     f.write('      This is line {}       \n'.format(i))

#Append a file
f = open('example.txt','a')
for i in range(10):
    f.write('*******This is line {}\n'.format(i+1))

#Open write
# with open("example.txt",'w') as f:
# 	for i in range(10):
# 		f.write("Hello World {}\n".format(i))

#Read from file
# f = open('example.txt','r')
# a=f.readlines()
# print(a)
#print(list(a))

# for i in fl:
# 	print (i.strip())

# with open("test.txt",'r') as f:
# 	for i in f:
# 		print(i.strip())

#Read From file in One Line
#for i in open('test.txt','r'): print (i.strip())

#---------------------------------------------

#Challenge
import sqlite3

db= sqlite3.connect('example.db')
subjectlist=db.execute('SELECT * FROM subject ORDER BY subjects')

a=list(subjectlist)
print(a)

for i in a:
	b=list(i)
	print(b)

f = open("subjects.txt",'a')
for i in a:
	b=list(i)
	#print(b)
	f.write("{}\t{}\t {}\n".format(b[0],b[1],b[2]))
 	


# f = open("subjects.txt",'w')
# f.write("------\n")
# for r in subjectlist:
# 	#f.write("{}\t{}\t {}\n".format(r[0],r[1],r[2]))
# 	f.write(r,"\n")




