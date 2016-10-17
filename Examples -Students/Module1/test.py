"""print("Hello World---------")
print("Hello World---------")
print("Hello World---------")
print("Hello World---------")
print("Hello World---------")
print("Hello World---------")
"""

# import os, sys

# # Open a file
# path = "c://"
# dirs = os.listdir( path )

# # This would print all the files and directories
# for file in dirs:
#    print(file)


#print("My name is Harold")
# a= 20.223456
# b= 12.167865

# c= a * b
# print(c)

# word1="Today have slight  haze only"
# b=word1.split()
# print(b)
# print(len(b))

#from numba import jit, int32

#@jit(int32(int32, int32))
#def f(x, y):
     ## A somewhat trivial example
     #return x + y

#print(f(10,20))
#----------------------------------------------

#import numpy as np
#import matplotlib.pyplot as plt
#g = np.random.randn(100)
#plt.hist(g, bins=10)
#plt.show()
#-----------------------------------
#import numpy as np
#print(np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int))

#import numpy as np
#print(10*np.random.random((3,4)))
#a = np.floor(10*np.random.random((3,4)))
#print(a)
#c=a.ravel()
#print(c)

import pandas as pd
import numpy as np

#s = pd.Series([1,3,5,6,2,4,6,2])
#print(s.value_counts())

#s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
#print(s[2])

#a = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
#b = pd.Series([4, 3, 2, 1], index=['d', 'c', 'b', 'a'])
#print(a + b)		# different from Python list
#print(a - b)
#print(a * b)
#print(a/b)

a = pd.DataFrame([[1,2],[3,4]],index=[1,2],columns=['a','b'])
b = pd.DataFrame([[4,3],[2,1]],index=[2,1],columns=['b','a'])
print(a)
print(b)
print(a + b)		# different from Python list
print(a - b)
print(a * b)
print(a/b)

