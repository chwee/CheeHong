class Employee:

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
   
   
   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)


class Rectangle:
    def __init__(self, height, width):
        self.h = height
        self.w = width
    def perim(self):
        return (2 * self.h) + (2 * self.w)
    def area(self):
        return self.h * self.w
    def isSquare(self):
        return (self.h == self.w)


