import employee

company=[]
emp1 = employee.Employee("Zara", 2000)
company.append(emp1)
emp2 = employee.Employee("Manni", 5000)
company.append(emp2)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee", len(company))


rect1 = employee.Rectangle(10,20)
print(rect1.perim())