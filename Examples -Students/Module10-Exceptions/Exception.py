#Exception

# try:
#     i = int(input('Enter an integer: '))    
#     print("You enter ",i)
# except:
#     print("This is a not an integer")
    
#----------------------------------------
# try:
# 	f = open('test888.txt','r')
# except:
#     print("file does not exist")
#-------------------------------------

# def readfile(file):
#     if file.endswith('.txt'):
#         f = open(file)
#         return f.readlines()
#     else:
#         raise ValueError("wrong extension")


# readfile('debug.dat')

#------------------------------------------------------------
#Challenge

# correct_number=10
# try:
# 	#guess = int(input('Guess a number : '))
# 	guess = 'A'
# 	if (guess == correct_number):
# 		print("good guess!")
# 	else:
# 		print("wrong guess ")
# except:
# 	print("Wrong input")


#-------------------------------------------------
#Challenge
# a = [1,2,3,"a",4,5,"b",6,7,"c"]
# b=[]

# for i in a:
# 	try:
# 		if (i > 0): b.append(i)
# 	except:
# 		pass

# print(b)