import numpy as np
import csv as csv
import matplotlib.pyplot as plt
import pandas as pd


#Importing CSV File Data.
readdata = csv.reader(open("pop_change.csv"))

#read into a object to save memory
print(readdata)

#for checking
# for row in readdata:
#   print(row)


# data = []
# for row in readdata:
#   data.append(row)
data = list(readdata)
#print(data)


Header = data[0]
data.pop(0)




#Displaying Our Beautiful Data.
#print(pd.DataFrame(data, columns=Header))

#But wait, I want to edit this data...!
Header.append("Difference")
for i in range(len(data)):
  diff = int(data[i][2]) - int(data[i][1])
  data[i].append(diff)

result= np.array(data)
print(result)
print(result.shape)

# # #print(pd.DataFrame(data, columns=Header))
# df=pd.DataFrame(data, columns=['STATE_OR_REGION', '1910_POPULATION', '2010_POPULATION',  'Difference'])
# #print(df['1910_POPULATION'])
# sample = list(df['1910_POPULATION'])
# print(sample)

N = len( data )
x = np.arange(1, N+1)
print(N)
print(x)
y = [ int(num3) for (s, num1,num2,num3) in data ]
print(y)
labels = [ s for (s, num1,num2,num3) in data ]
width = 1
bar1 = plt.bar( x, y, width, color="y" )
plt.ylabel( 'Population' )
plt.xticks(x + width/2.0, labels )
plt.show()

#An Extremely Basic Statistical Analysis.
# Two questions. How many people were living in the United States
# (according to this data) in 1910 and 2010?
# What was the mean and standard deviation for the 1910 population
#  data and the 2010 population data? 
#  These are things we should be able to answer easily.

pop1910 = []
pop2010 = []
for i in range(len(data)):
  pop1910.append(int(data[i][1]))
  pop2010.append(int(data[i][2]))

print("Total in 1910: %d" % (np.sum(pop1910))) 
print("Average in 1910: %d" % (np.mean(pop1910)))
print("Standard Deviation in 1910: %d" % (np.std(pop1910))) 

print("Total in 2010: %d" % (np.sum(pop2010))) 
print("Average in 2010: %d" % (np.mean(pop2010)))
print("Standard Deviation in 2010: %d" % (np.std(pop2010)))


#Displaying Data.

