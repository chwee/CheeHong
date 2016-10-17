# a = [7,8,9,10,'Test']
# print(a[2])
# print(c[-1])


#-----------------------
#List

#Slicing list
# a = [7,8,9,10,11] 
# print(a[1:3])
# print(a[1:])
# # # print(a[2:])
# # # print(a[:-1])
# print(a[:-2])
# print(a[:])
# print(a)


#-----------------------------------

#serach list
#method index() returns the lowest index in list that obj appears

# a =[5,4,3,2,1,4]
# print(a.index(4))
# print(5 in a)
# # print(7 in a)

# a=['A','B','C','D','E']
# print(a.index('D'))

#-------------------------------------

#Add element to list

#append to add last number
# a =[5,4,3,2,1]
# # a.append(6)
# print(a)

# #insert the number 
# a.insert(2,99)
# print(a)

#insert at second last index
# a.insert(-1,199)
# print(a)

#-------------------------
#remove elements
#a =[5,4,3,2,1]
# #remove is the value of the element in list
# a.remove(4)
# print(a)

# del a[1]
# print(a)

# #pop at last index
# a.pop()
# print(a)

# #pop at index
# a.pop(1)
# print(a)

#-------------------------------

#copy list

# a = [1,2,3,4,5]
# b = a.copy()

# print('a=',a)
# print('b=',b)

# a.append(6)
# print('a=',a)
# print('b=',b)


#-----------------------
#Extend the list
a = [1,2,3,4,5]
b = [6,7,8]

# a.append(b)
# print(a)
# c=a[5]
# print(c[0])

# c=a + b
# print(c)

# c=a*2
# print(c)

# a *= 3
# print(a)

# print(len(a))


#--------------------
# #Sort & Reverse List

# a = [5,2,3,4,1]
# a.sort()
# print(a)

# # a.sort(reverse=True)
# # print(a)

# #the org list is not modified
# a = [5,2,3,4,1]
# c=sorted(a)  
# print(a)
# print(c)

#change only indexing
# a = [5,9,2,3,4,1]
# a.reverse()
# print(a)
#--------------------------------------

#math on list

# a = [1,2,3,4,5,10,8,6,4,2,1]
# print('sum=', sum(a))
# print('min=',min(a))
# print('max=',max(a))
# print('len=',len(a))
# print('count=',a.count(2))
# print(2 in a)
# print(2 not in a)
# print(7 in a)


#----------------------------------

#Challnge
# #count A in letters
# letters =['A','C','C','A','T','T','G','A','C','A']
# print('A coun=', letters.count('A'))

# # #find out which location is first T 
# print('Loc T is ', letters.index('T'))

# # # # #copy from original letters
# # a=letters.copy()
# # print(a)

# # # # # remove G in new letters
# letters.remove('G')
# print(letters)

# # # # # insert A in location 3
# letters.insert(2,'A')
# print(letters)

# # # # reverse the order of new letters
# letters.reverse()
# print(letters)

#----------------------------------------------
# Challenge Examples
#Extract all the even numbers in the List

# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# b=list()

# for x in a:
# 	if x%2 ==0:
# 		b.append(x)

# print(b)

#--------------------------------------------------
#Challenge Example

# from graphics import *


# def main():
#     a=[(20,20,'red'), (50,50,'blue'),(80,80,'yellow')]

#     win = GraphWin('Cicles', 200, 200) # give title and dimensions
#     #win.yUp() # make right side up coordinates!

#     for b in a:
#         c=list(b)
#         cir = Circle(Point(c[0],c[1]), 20)
#         cir.setFill(c[2])
#         cir.draw(win)


#     message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
#     message.draw(win)
#     win.getMouse()
#     win.close()

# main()

#---------------------------------------------------------------
# letters =['A','C','C','A','T','T','G','A','C','A']
# print(len(letters))
# letters1=['ACCATTGACA']
# print(len(letters1))
# test='one two three'
# print(test.split())
