#Conditions

#if else-----------------------------------------------

# a=15
# b=10

# #print(a<b)

# if (a<b):
# 	print("--------------")
# 	print("a is smaller than b")
# 	print("----------------")
# else:
# 	print("a is larger than b")
#-----------------------------------------------------------

#if else-

# a='TestA'
# b='TestB'

# #print(a<b)

# if (a==b):
# 	print("same")
# else:
# 	print("different")


#------------------------------------------

#if elif else
# a=5
# b=5
# if (a < b):
# 	print("a is smaller than b")
# elif (a >b):
# 	print("a is larger than b")
# elif (a== b):
# 	print("a is same as b")
# else:
# 	print("Not in check condition")

#-----------------------------------------

#ternary operator
# order_total  = 120
# discount = 25 if order_total > 100 else 0

# print(discount)

#--------------------------------------------

# #Callenge
# g= 'A'
# #g= input("Enter here:")
# if g == 'A':
# 	print("Excellent!")

# elif g == 'B':
#     print('Well done!')
# elif g == 'C':
#     print("Good job!")
# else:
#     print("Non of the grade")
#----------------------------------------


#Loop-----------------------------------------

#while
# x = 0

# while (x < 5):
# 	print("x = ", x)
# 	#x = x + 1
# 	x+=1
#------------------------------

# Challenge Fibonacci while loop
#1, 1, 2, 3, 5, 8, 13, 21, 34, …

# a, b = 0, 1
# while b < 100:
#     print(b)
#     a, b = b, a + b

#-------------------------------

#For loop
# a=[1,2,3,4,5]
# for x in a:
# 	print("x = ",x)

# for x in range(1,20,2):
# 	#a= x+ 3
# 	print("x=", x)

# fruits = ['Durian', 'Banana','Orange','Apple']

# for today_fruit in fruits:
# 	print("Today food is ", today_fruit)

#-----------------------------------

#range

# a=list(range(2,20))
# b=tuple(range(2,20))
# # c=set(range(2,20,2))
# print(a)
# print(b)
# # print(c)

# for x in range(2,20,2):
# 	print(x)


#---------------------------------

#Challenge Square Numbers List
# a=[]
# for i in range(1,11):
# 	a.append(i*i)
# 	print(i*i)

#print(a)
# print(a.index(64))




#-------------------------------
#iterate through seq list
#Enumerate
# person = ['Alfred','Ally','Belinda']
# height = [170,160,155]
# for i,name in enumerate(person):
# 	h = height[i]
# 	print("The height of {} is {}cm".format(name,h))

# for i,name in enumerate(person):
# 	print(i, name)

#----------------------------------------------

#Zip
#ex1
# a = [1,2,3,4,5,6]
# b = ['a','b','c','d','e','f']

# c = zip(a,b)
# for i in c:
#     print(i)

#ex2
# a = ['Ally','Belinda','Jane']
# b = [170,159,161]
# c = [60,55,45]

# for name,height,weight in zip(a,b,c): 
#  	print("The height and weight of {} is {} and {}".format(name,height,weight))

#---------------------------------------

#Break Continue
# for x in range(1,5):
# 	if (x == 3): 
# 		break
# 	print("x = ", x)

# for x in range(1,5):
# 	if (x == 3): 
# 		continue
# 	print("x = ", x)

#--------------------------------------

# i=5
# print(i % 5)
# print(i/5)

#Loop with Else

# #x = [1,2,3,4,5,6,7]
# x = [1,2,3,4]

# for i in x:
# 	if i % 5 == 0:
# 		break
# 	else:
# 		print(i)
# else:
# 	print("complete Loop")


#----------------------------------
#Challnege prime number

#XXXXXXXXXXXXXXXXXX
# for num in range(1,101):
#     for i in range(2,num):
#         if (num%i==0):
#             break
#         else:
#             print(num)
#             break

# for n in range(1,101):
# 	status = True
# 	if n < 2:
# 	    status = False
# 	else:
# 	    for i in range(2,n):
# 	        if n % i == 0:
# 	            status = False

# 	    if status:
# 	        print(n, '', sep=',', end='')

#------------------------------------

# lower = 1
# upper = 100

# for num in range(lower,upper + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#    	is_prime = True
#     #(Prime)num cannot be dividable in range
#    	for i in range(2,num):
#    		if (num % i) == 0:
#    			is_prime =False
#    			break
#    	if is_prime == True:
#    		print(num)

#------------------------------------
#using for else
# lower = 1
# upper = 100
# primenum=[]
# for num in range(lower,upper + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#     #(Prime)num cannot be dividable in range
#     #append num into the list primenum
#    	for i in range(2,num):
#    		if (num % i) == 0:
#    			break
#    	else:
#    		primenum.append(num)

# print(primenum)   		
#-----------------------------------------
# for num in range(10,20):  
#    for i in range(2,num): 
#       if num%i == 0:      
#          j=num/i          
#          print ('%d equals %d * %d' % (num,i,j))
#          break 
#    else:                  
#       print(num, 'is a prime number')


#--------------------------------------------------------- 	  
#Bioinfomatics
#Not using functionmethod
# dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
# n = len(dna_list[0])
# A = [0]*n
# T = [0]*n
# G = [0]*n
# C = [0]*n
# for dna in dna_list:
# 	for index, base in enumerate(dna):
# 		if base == 'A':
# 			A[index] += 1
# 		elif base == 'C':
# 			C[index] += 1
# 		elif base == 'G':
# 			G[index] += 1
# 		elif base == 'T':
# 			T[index] += 1
   
# print("index 0  1  2  3  4")
# print('A  ',A)
# print('C  ',C)
# print('G  ',G)
# print('T  ',T)






#-----------------------
#using functionmethod
# def freq_lists(dna_list):
#     n = len(dna_list[0])
#     A = [0]*n
#     T = [0]*n
#     G = [0]*n
#     C = [0]*n
#     for dna in dna_list:
#         for index, base in enumerate(dna):
#             if base == 'A':
#                 A[index] += 1
#             elif base == 'C':
#                 C[index] += 1
#             elif base == 'G':
#                 G[index] += 1
#             elif base == 'T':
#                 T[index] += 1
#     return A, C, G, T

# dna_list = ['GGTAG', 'GGTAC', 'GGTGC']
# A, C, G, T = freq_lists(dna_list)
# print("index 0  1  2  3  4")
# print('A  ',A)
# print('C  ',C)
# print('G  ',G)
# print('T  ',T)

#----------------------------------------------------


