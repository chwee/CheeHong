#@Displaying Data.
#Importing XLS File Data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd


wb = xlrd.open_workbook('grades.xls')
sheet = wb.sheet_by_index(0)

grades = []

for i in range(sheet.nrows):
    grades.append(int(sheet.cell(i,0).value))

#Histograms in Matplotlib.pyplot.
def summary(data):
    print("Max: %d" % (np.amax(data)))
    print("Min: %d" % (np.amin(data)))
    print("Mean: %d" % (np.mean(data)))
    print("Stdev: %d" % (np.std(data)))
   
summary(grades)
plt.hist(grades, bins=30)
#plt.hist(grades, bins=[65,70, 75, 80, 85, 90, 95, 100])
plt.show()

#Pie Charts in matplotlib.pyplot.

failed = 0
passed = 0

for grade in grades:
  if grade < 75:
    failed += 1
  else:
  	passed += 1

#v1
plt.pie([passed, failed])
plt.show()

#v2
# plt.pie([passed, failed], labels=["passed","failed"])
# plt.show()

#v3 explode
# plt.pie([passed, failed], labels=["passed","failed"], explode = (0,0.05))
# plt.show()

#shadow
# plt.pie([passed, failed], labels=["passed","failed"],explode = (0,0.05), shadow = True)
# plt.show()

#title
# plt.pie([passed, failed], labels=["passed","failed"],explode = (0,0.05), shadow = True)
# plt.title('Class Pass/Fail.')
# plt.show()



