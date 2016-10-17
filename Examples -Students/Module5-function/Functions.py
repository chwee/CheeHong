#Functions----------

# def square(x):
# 	return x*x

# print(square(9))

# def sum(a,b,c):
# 	return a+b+c

# print(sum(1,2,3))



# def square(x):
# 	a= x*x
# 	return a

# print(square(3))

# x=3
# a= x*x
# print(a)

#--------------------------------------
#Challenge

#taxi fare = booking fee + starting price+ distance*cost per km



# #CostPerkm= 0.50
# def taxifare(bookfee, startpr, dist, CostPerkm=0.5):
# 	total= bookfee+startpr+ dist * CostPerkm
# 	return total

# total2=taxifare(25,2,10,1.1)
# print("fare =",total2)

# total1=taxifare(25,2,10)
# print("fare {}".format(total1))
# print("fare =",total1)
#----------------------------------------------------------

#challenge Grocery
#function to return the discount and the tax for grocery purchase

# def GetDiscountTax(order):
# 	discount = 25 if order > 200 else 0
# 	tax = 0.07*(order-discount*order/100)
# 	return(discount, tax)

# getDis, getTax=GetDiscountTax(100)
# print("Discount ={} Tax={}".format(getDis, getTax))

#---------------------------------------------------

# def rect(a=3,b=5):
# 	c= a*b
# 	return c

# print(rect())
# # print(rect(a=1,b=8))

#-----------------------------------------
#Challenage Min Value
# l=[5, 6, 2,3]

# x = l[0]
# for i in l:
# 	if i < x:
# 		x = i
# print(x)
# print(min(l))

#-----------------------------------------------------
#Function parameters

# def myadd(a,b,*c,**d):
# 	sum = a+b
# 	for i in c:
# 		sum = sum + i
# 	for k in d:
# 		sum = sum + d[k]
# 	return sum

# aa = myadd(1,2,3,4,5,6,a1=7,a2=8,a3=9,a4=10)

#the asterisk in front of the vals parameter means any other 
#positional parameters

# def lessThan(cutoffVal, *vals) :
#     ''' Return a list of values less than the cutoff. '''
#     arr = []
#     for val in vals :
#         if val < cutoffVal:
#             arr.append(val)
#     return arr
# print(lessThan(10, 2, 17, -3, 42))

#A double asterisk in front of the dict parameter below means
#any other named parameters. This time, Python will give them 
#to us as key/value pairs in a dictionary.

# def printVals(prefix='', **dict):
#     # Print out the extra named parameters and their values
#     for key, val in dict.items():
#         print('%s [%s] => [%s]' % (prefix, str(key), str(val)))

# printVals(prefix='..', foo=42, bar='!!!')
# printVals(prefix='..', one=1, two=2)
#--------------------------------------------
#Decorator

# def time_this(original_function):      
#     def new_function(*args,**kwargs):
#         import datetime                 
#         before = datetime.datetime.now()                     
#         x = original_function(*args,**kwargs)                
#         after = datetime.datetime.now()                      
#         print("Elapsed Time = {0}".format(after-before))      
#         return x                                             
#     return new_function                                   

# @time_this
# def func_a(stuff):
#     import time
#     time.sleep(3)

# func_a(1)

#---------------------------------------
# def decorator(func):
# 	def wrapper():
# 		print("Hello")
# 		print(func("Hi there...."))
# 		print("How r you?")
 
# 	return wrapper
 
# # def some_random_function(saying):
# # 	return saying
 
# # decorated_function = decorator(some_random_function)
# # decorated_function()

# @decorator
# def some_random_function(saying):
# 	return saying
 
# some_random_function()

#---------------------------------------
#decorator
# def helloSolarSystem(original_function):
#     def new_function():
#         original_function()  # the () after "original_function" causes original_function to be called
#         print("Hello, solar system!")
#     return new_function
     
# def helloGalaxy(original_function):
#     def new_function():
#         original_function()  # the parentheses after "original_function" cause original_function to be called
#         print("Hello, galaxy!")
#     return new_function
 
# @helloGalaxy
# @helloSolarSystem
# def hello():
#     print ("Hello, world!")
 
# # Here is where we actually *do* something!
# hello()

#---------------------------------------------
# def helloSolarSystem(original_function):
#     def new_function():
#         original_function()  # the () after "original_function" causes original_function to be called
#         print("Hello, solar system!")
#     return new_function
     
# def helloGalaxy(original_function):
#     def new_function():
#         original_function()  # the parentheses after "original_function" cause original_function to be called
#         print("Hello, galaxy!")
#     return new_function

# def hello():
#     print ("Hello, world!")
# hello = helloSolarSystem(hello)
# hello = helloGalaxy(hello)

# hello()
#------------------------------------------

#Let’s pretend that the goal of this decorator is to format the returned number into a string representing a float with a 2 digits precision. The implementation will be as follow:

def format_result(func):
    def wrapper(x, y):
        ''' Format a float to a 2 digits precision '''
        return '{:.2f}'.format(func(x, y))
    return wrapper

@format_result
def divide(x, y):
    ''' Divide x by x '''
    return float(x) / float(y)

print(divide(3.0, 4.5))
