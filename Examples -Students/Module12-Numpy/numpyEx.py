#Numpy
import numpy as np

#CREATE--------------------------------------------
#create 1D numpy array

# a = np.array([2,3,4])
# print(a)
# print(a[1])

#Array Attributes
# print(a.ndim)		# dimension of array p
# print(a.shape)	# size of array dimension
# print(len(a))		# length of array 
# print(a.dtype)		# data type of array

#-------------------------------------------------
#2x2 array
# a = np.array([[2,3,4],[6,7,8]])
# print(a)
# print(a[1,1])


# print(a.ndim)		# dimension of array p
# print(a.shape)	# size of array dimension
# print(len(a))		# length of array 
# print(a.dtype)		# data type of array

#----------------------------------------------
#Special Array Creation
# a=np.zeros( (3,4) )
# b=np.ones( (2,3,4), dtype=np.int16 )
# c=np.empty( (2,3) ) 
# print(a)
# print(b)
# print(c)
#-----------------------------------------------
#Challenge
# import numpy as np
# a = np.array([2,3,-2,-3,2,6,-3,4,-3,5,-6,5,5,-2])
# b=[]
# for i in a:
# 	if(i>0):
# 		b.append(i)

# print(b)
# print(sum(b))





#----------------------------------------
#create array using funtion

# def f(x,y):
#     return 10*x+y
# b = np.fromfunction(f,(5,4),dtype=int)

# print(b)

#-------------*********************---------------------
#Create Sequence  1D
# v=np.arange(10, 20,2)
# print(v)

# v= np.linspace(0,10,5)
# print(v)
# print(v[2:4])
#------------------------------------------

# import random as random
# vv= np.random.standard_normal((5,4))
# print(vv)
# print(vv[2:5,1])
# print(vv[2:5,1:2])
#------------------------------------------
#Reshape 1D to 2D
# print(np.arange(1, 10))
# a = np.arange(1, 10).reshape(3, 3)
# print(a)
# print(a[1:,1: ])

# h = np.arange(12).reshape(4,3)
# print(h)

#OPERATION----------------------------------------
#----------------------------------------------
# 1D operation
# a = np.array([1,1,1,1])
# b = np.array([2,2,2,2])
# print(a+b)		# different from Python list
# print(a-b)		# can't do using Python list
# print(a*b)
# print(a/b)

#List add two List
# a=[1,1,1,1]
# b=[2,2,2,2]
# print(a+b)
#-----------

#2D operation
# a = np.array( [[1,1], [2,2]] )
# b = np.array( [[3,3], [4,4]] )
# print(a)
# print(b)
# print(a+b)			# different from Python list
# print(a-b)			# can't do in Python list
# print(a*b)
# print(a/b)

#Add two Lists
# a = [[1,1], [1,1]] 
# b = [[2,2], [2,2]] 
# print(a)
# print(b)
# print(b+a)

#----------------------------------------------
#Statistical Operations
# a = np.array( [[1,2,3,4], [5,6,7,8]] )
# print(np.mean(a))
# print(np.mean(a,axis=0))		# column mean 
# print(np.mean(a,axis=1) )	#row mean

# print(np.var(a))
# print(np.std(a))   #square root of var
#-----------------------------------------

#Compound Operators
# a = np.ones((2,3), dtype=int)
# a *= 3
# print(a)
# a = np.ones((2,3), dtype=int)
# a += 3 
# print(a)
#-----------------------------------------
#Mathematical Functions
# a = np.array([1,2,3,4])
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.sin(a))
# print(np.cos(a))


#INDEXING---------------------------------------
#----------------------------------------

#1D Array Indexing
# a = np.arange(10)
# print(a)
# print(a[2])
# print(a[-1])
#-----------------------------------------

#2D Array Indexing
# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(a)
# print(a[2,2])
# print(a[-1,-1])  #12
# print(a[-1,-2])  #11
# print(a[-2,-2])  #8

#-------------------------------------------
#Logical Indexing
# a =np.array([3,5,1,10])
# print(a%5==0)
# print(a[a%5==0])
# print(a>1)
# print(a[a>1])

#------------------------------------
#Challenege
#List out all the non-negative elements in the list
#[2,3,-2,-3,2,6,-3,4,-3,5,-6,5,5,-2]

# a = np.array([2,3,-2,-3,2,6,-3,4,-3,5,-6,5,5,-2])
# print(np.sum(a[a>0]))

#SLICING-----------------------------------------
#-----------------------------------------------
#1D Array Slicing

# a = np.arange(10)
# print(a[2:5])
# print(a[:6:2])
# print(a[ : :-1])
# print(a[::])
# print(a[::5])

#--------------------------------------------
#2D Array Slicing
# def f(x,y):
#     return 10*x+y
# b = np.fromfunction(f,(5,4),dtype=int)
# print(b)
# print(b[0:3, 1])  #row 0 to 2 ,col 1
# print(b[ : ,1])   #row all , col 1
# print(b[1:3, : ]) #row 1 to 2, col all
# print(b[-1])

#------------------------------------------
#Dot
# A = np.arange(10)
# print( A[...])

# B = np.reshape(np.arange(9),(3,3))
# print(B[...])
# print(B[0,...])  #row 0
# print(B[...,1])  #Column 1


# C = np.reshape(np.arange(2*3*4),(2,3,4))
# print(C)
# print(C[1,...,1])
# print(C[0,Ellipsis,0])


#-----------------------------------------
#Iterating
# def f(x,y):
#     return 10*x+y

# b = np.fromfunction(f,(5,4),dtype=int)
# print(b)

# for row in b:
#     print(row)

#-------------------------------------------------
#Shape Manipulation

#Flatten the Array
# a = np.floor(10*np.random.random((3,4)))
# print(a)
# print(a.ravel())

#Reshape the Array
# a = np.floor(10*np.random.random((3,4)))
# print(a)
# a.shape = (6, 2)
# print(a)
# a.resize((2,6))
# print(a)

#Stacking Array
# [[1 1]
#  [2 2]
#  [3 3]]
# [[4 4]
#  [5 5]
#  [6 6]]
# a = np.array([[1,1],[2,2],[3,3]])
# b = np.array([[4,4,],[5,5],[6,6]])

# print(np.vstack([a,b]))
# print(np.hstack([a,b]))

#------------------------------------
#Statistics
#Simple Statistics - 1
# a = np.array( [[1,2,3,4], [5,6,7,8]] )
# print(np.sum(a, axis=0))		# column sums
# print(np.sum(a, axis=1))	# row sums
# print(np.mean(a, axis=0))	# column mean
# print(np.mean(a, axis=1))	# row mean
# print(np.diff(a, axis=0))		# column diff
# print(np.diff(a, axis=1))		# row diff
# print(np.prod(a, axis=0))		# column prod
# print(np.prod(a, axis=1))		# row prod

# print(np.std(a, axis=0))		# column std dev
# print(np.std(a, axis=1))	# row std dev
# print(np.var(a, axis=0))		# column var
# print(np.var(a, axis=1))		# row var

#--------------------------------------------
#Random Numbers
# print(np.random.seed(20))
# print(np.random.rand(5)	)				# uniform dist
# print(np.random.randint(1,6,5))		# uniform dist	
# print(np.random.randn(5))				# normal dist
# #print(np.random.binomial(n,p,3))		# binomial dist
# print(np.random.poisson(lam=2,size=2)) # poisson dist
# #print(np.random.shuffle(1:10))


#__END______________________________________
#------------------------------------------
# a = np.array([[1,2,3],[3,4,5],[6,7,8]])
# print(a[1, 1:])
# b= a[:,:].copy()
# b[1,1]=0
# print(b)
# print(b>2)

# a = np.array([1,2,3,4,5,6])
# print(a)
# bool_index = a >2
# print(a[bool_index])

# a = np.array([[1,2,3],[3,4,5],[6,7,8]])
# bool_index = a >2
# print(a[bool_index])
# b=list(a[bool_index])
# print(b[2])

# a = np.array([[1.1,2.1,3.1],[3.1,4.1,5.1],[6.1,7.1,8.1]])
# a[a>0.5] = a[a>0.5] + 1.0
# print(a)

# def f(x,y):
#     return 10*x+y
# b = np.fromfunction(f,(5,4),dtype=int)
# print(b)








#-----------------------------------------------------

# X = np.array(range(24))
# Y = X.reshape((3,4,2))
# print(Y)
# print(Y.shape)

# print(Y[:1,:2,:].shape)

#----------------------------
#Numpy Vs List
import time
size_of_vec = 1000000
def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    print(Z)
    return time.time() - t1
def numpy_version():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    print(Z)
    return time.time() - t1

t1 = pure_python_version()
t2 = numpy_version()
print('t1=',t1)
print('t2=',t2)
