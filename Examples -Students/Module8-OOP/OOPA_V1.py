#OOP V1

#Class Example
# class Person():

#     def __init__(self, name, age,ID):
#         self.name = name
#         self.age = age
#         self.ID= ID

#     def is_old(self):
#         return self.age

        
# Hardy = Person('G. H. Hardy', 45,123)
# # # age=23
# print(Hardy.is_old())
# # print(person.name)
# print(person.__ID)

# person1 = Person('Tim', 12)
# # age=23
# print(person1.is_old())
#----------------------------------------------------------
#Example of Class Cal
# class Cal():

# 	def __init__(self, num1, num2):
# 		self.a= num1
# 		self.b= num2

# 	def add()
# 		return self.a + self.b

# 	def minus(self)
# 		return self.a - self.b

# 	def multiply(self)
# 		return self.a*self.b

# 	def divide(self)
# 		return self.a/self.b

# a=2
# b=3
# CalA= Cal(a,b)
# print(CalA.add())






#----------------------------------------------------------

#Challenge

# class Square:
# 	def __init__(self, length):
# 		self.h = length
# 		self.w = length

# 	def perim(self):
# 		return (2 * self.h) + (2 * self.w)
# 	def area(self):
# 		return self.h * self.w
	
    
    
# x = Square(3)
# print(x.area())

# #x= Square(3)

# # print("perim=",x.perim())
# print("area=",x)


#---------------------------------------------

#Challenge
#Method 1
# class Employee:
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary)


# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)

# emp1.displayEmployee()
# emp2.displayEmployee()

# print("Total Employee", Employee.empCount)

#---------
#Method 2
# class Employee():

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
     
#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary)

# company=[]
# emp1 = Employee("Zara", 2000)
# company.append(emp1)
# emp2 = Employee("Manni", 5000)
# company.append(emp2)

# emp1.displayEmployee()
# emp2.displayEmployee()

# print("Total Employee", len(company))




#----------------------------------------------------------------
#Inheritance

#Example 1
# class Person():
# 	def __init__(self, name):
# 		self.name = name

# 	def get_details(self):
# 		return self.name

# 	def get_more(self):
# 		return print("Test msg")

   
# class Student(Person):
#     def __init__(self, name, branch, year):
#         Person.__init__(self, name)
#         self.branch = branch
#         self.year = year

#     def get_details(self):
#     	return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)

# person1 = Person('Sachin')
# student1 = Student('Kushal', 'CSE', 2005)


# print(person1.get_details())
# print(student1.get_details())
# print(student1.get_more())

#==============================
#Example 2 inheritance
#----- Parent class: person --------
# class person:
#     def __init__(self,first,last):
#         self.firstName = first
#         self.lastName = last

#     def getName(self):
#         return self.firstName + " " + self.lastName

# #----- child class: Employee inherited from person --------
# class Employee(person):
#     def __init__(self,first,last,staffNum):
#         person.__init__(self,first,last)
#         self.staffNum = staffNum

#     def getEmployee(self):
#         return self.getName() + ": " + self.staffNum
# #----- child class: Employee inherited from person --------
# class Boss(person):
#     def __init__(self,first,last,title):
#         person.__init__(self,first,last)
#         self.title = title

#     def getBoss(self):
#         return self.getName() + ": Employee ID: " + self.title

# #----- instantiate class --------    
# person_1 = person("Math", "Hoang")
# Employee_1 = Employee("Math", "Hoang", "12344")
# Employee_2 = Employee("Blog", "spot", "43211")
# Boss_ = Boss("Mathhoang", "Blogspot.com", "CEO")

# #------ print out information ------
# print(person_1.getName())
# print(Employee_1.getEmployee())
# print(Employee_2.getEmployee())
# print(Boss_.getBoss())



#==============================
#XXXXXXXXXXXXXXXXXXXXXX
#---------------------------------------------------
#Inheritance vs Composition
#Composition uses an instance of the class

# class Math:
#    def __init__(self,x,y):
#       self.x=x
#       self.y=y
#    def add(self):
#       return self.x + self.y
#    def subtract(self):
#       return self.x- self.y

# class Math2:
#    def __init__(self,x,y):
#       self.x=x
#       self.y=y
#    def multiply(self):
#       return self.x * self.y
#    def divide(self):
#       return self.x/ self.y

# class Math3:
#    def __init__(self,x,y):
#       self.x=x
#       self.y=y
#       self.m1 = Math(x,y)
#       self.m2 = Math2(x,y)
#    def power(self):
#       return self.x**self.y
#    def add(self):
#       return self.m1.add()
#    def subtract(self):
#       return self.m1.subtract()
#    def multiply(self):
#       return self.m2.multiply()

# calculator = Math3(5,6)
# print("5+6=",calculator.add())
# print("5*6=",calculator.multiply())
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#-----------------------------------------------------
#Initializing Child Class
# class Book:
#     def __init__(self, title, publisher, pages):
#         self.title = title
#         self.publisher = publisher
#         self.pages = pages

# class Ebook(Book):
#     def __init__(self, title, publisher, pages, format):
#         Book.__init__(self,title, publisher, pages)
#         self.format = format


#-------------------------------------------------------
#Multiple Inheritance    /Super

# With Super
# class First(object):
# 	def __init__(self):
# 		pass

# 	def func1(self):
# 		return print("First obj func1")

# class Second(object):
# 	def __init__(self):
# 		pass

# 	def func2(self):
# 		return print("Second obj func2")

# class Third(First, Second):
# 	def __init__(self):
# 		super(Third, self).__init__()
# 		print("Third init")

# c= Third()
# c.func1()
# c.func2()
#----------------------------------------
# class A(object):
#     def __init__(self, a, b):
#         print('Init {} with arguments {}'.format(self.__class__.__name__, (a, b)))

# class B(object):
#     def __init__(self, q):
#         print('Init {} with arguments {}'.format(self.__class__.__name__, (q)))

# class C(A, B):
#     def __init__(self):
#         # Unbound functions, so pass in self explicitly
#         A.__init__(self, 1, 2)
#         B.__init__(self, 3)

# c=C()

#----------------------


#---------------------------------------
#Challenge Rectangle
# class Square:
#     def __init__(self, length):
#         self.h = length
#         self.w = length
#     def perim(self):
#         return (2 * self.h) + (2 * self.w)
#     def area(self):
#         return self.h * self.w

# class Rectangle(Square):
#     def __init__(self, length,width):
#         Square.__init__(self,length)
#         #self.h= length
#         self.w= width

# RectA= Rectangle(20,5)
# print("RectA area=",RectA.area())
# print("RectA perim", RectA.perim())


# #----------------------------------------------

#Polymerism


#Polymorphism in Python with a function:

#Example 1
# class Animal():
# 	def sound(self):
# 		pass

# class Bear(Animal):
#     def sound(self):
#         print("Groarrr")
 
# class Dog(Animal):
#     def sound(self):
#         print("Woof woof!")
 
# def makeSound(Animal):
#     Animal.sound()

# bearObj = Bear()
# dogObj = Dog()
 
# makeSound(bearObj)
# makeSound(dogObj)


#Example 2
# class Car:
#     def __init__(self, name):    
#         self.name = name
 
#     def drive(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
#     def stop(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
# class Sportscar(Car):
#     def drive(self):
#         return 'Sportscar driving Zoom Zoom!'
 
#     def stop(self):
#         return 'Sportscar breaking!'
 
# class Truck(Car):
#     def drive(self):
#         return 'Truck driving slowly because heavily loaded.'
 
#     def stop(self):
#         return 'Truck breaking!'
 
 
# cars = [Truck('Bananatruck'),
#         Truck('Orangetruck'),
#         Sportscar('Z3')]
 
# for car in cars:
#     print(car.name + ': ' + car.drive())
#-----------------------------------------------
#demo without polymorphism
# class Car:
#     def __init__(self, name):    
#         self.name = name
 
#     def drive(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
#     def stop(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
# class Sportscar():
# 	def __init__(self, name):
# 		self.name = name
	
# 	def drive(self):
# 		return 'Sportscar driving Zoom Zoom!'

# 	def stop(self):
# 		return 'Sportscar breaking!'
 
# class Truck():
# 	def __init__(self, name):
# 		self.name = name
# 	def drive(self):
# 		return 'Truck driving slowly because heavily loaded.'
# 	def stop(self):
#  		return 'Truck breaking!'

# cars = [Truck('Bananatruck'),Truck('Orangetruck'),Sportscar('Z3')]
 
# for car in cars:
#     print(car.name + ': ' + car.drive())




#-----------------------------------------------
#Challenege: Inheritance 

# class Employee:
#    empCount = 0
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary)

# class EmployeeFulltime(Employee):
# 	def __init__(self, name, salary, leaves):
# 		Employee.__init__(self, name, salary)
# 		self._leaves = leaves 

# class EmployeeParttime(Employee):
# 	def __init__(self, name, salary, Hourlyrate):
# 		Employee.__init__(self, name, salary)
# 		self._Hourlyrate = Hourlyrate 


# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)

# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee", Employee.empCount)



