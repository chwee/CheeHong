#Lambda ---------------------------------------------------
# def f(x):	
# 	return x**2

# f = lambda x: x**2
# print(f(3))

# #chanllenge------------------------

# def f(x,y):
#     return 10*x+y

# f = lambda x,y: 10*x+y

# print(f(3,2))

#----------------------------------------

#Map   ##################################################
# a = [3,4,5,6,7]
# f = lambda x:x**2

# d=[]
# for c in a:
# 	d.append(f(c))
# print(d)


# print(map(f,a))
# print(list(map(f,a)))

#use normal method
# def f(x):
# 	return x**2

# a=[3,4,5,6,7]
# b=[]
# for i in a:
# 	b.append(f(i))
# print(b)

#Challenge----------------------------
# f = lambda x,y:10*x+y
# a = [0,1,2,3]
# b = [2,4,6,8]

# print(list(map(f,b,a)))

#----------------------------------




#Filter  ###############################

a= [1,2,3,4,5,6,7,8,9,10]
f = lambda x: x%3
b = filter(f,a)
print(list(b))

#------------------------------------
#Challenge(1)filter
# a = [1, 6, 3, 8, 4, 9]
# f= lambda x: x<5
# b= filter(f,a)
# print(list(b))


#----------------------------------
#challenge(2)

# def recur_fibo(n):
#    """Recursive function to
#    print Fibonacci sequence"""
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# # take input from the user
# #nterms = int(input("How many terms? "))
# nterms = 25

# # check if the number of terms is valid

# print("Fibonacci sequence:")
# for i in range(nterms):
#    print(recur_fibo(i))


# Explanation----------------------
# F(0)              0
# F(1)              1
# F(2)=F(1)+F(0)    1
# F(3)=F(2) +F(1)   2
# F(4)=F(3) +F(2)   3
# F(5)=F(4) +F(3)   5
# F(6)=F(5) +F(4)   8

#------------------------------------------

