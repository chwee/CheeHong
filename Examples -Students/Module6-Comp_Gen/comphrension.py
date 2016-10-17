#comprehensions

# a=[n*n for n in range(10000) if n%2==0]
# print(a)


# b=[]
# for n in range(10000):
# 	if(n%2==0):
# 		b.append(n*n)
# 	else
# 		pass
# print(b)

# b=[]
# for n in range(10000):
# 	b.append(n**2)
# print(b)


# a=[n ** 2 for n in range(10)]
# print(a)

# b=[n ** 2 for n in range(10) if not n % 2]
# print(b)


# a=(n*n for n in range(10000) if n%2==0)
# print(a)
# print(list(a))



#-------------------------------------------------
#Challenge
# Use comprehension method to extract the first letter of each word in the sentence below
# sentence = 'Today is a good day'

# sentence = 'Today is a good day'
# sentence_slpit= sentence.split()
# print(sentence_slpit)
# items = [ word[0] for word in sentence_slpit]
# print(items)

# sentence = 'Today is a good day'
# items = [ word[0] for word in sentence.split()]
# print(items)


# sentence = 'Today is a good day'
# sentence_slpit= sentence.split()
# print(sentence_slpit)
# items = [ word[0] for word in sentence_slpit if word.count('a') >0]
# print(items)


#-----------------------------------------------------------
#Nested comprehensions

# items = 'ABCDE'
# pairs = []
# for a in range(len(items)):
#     for b in range(a, len(items)):
#         pairs.append((items[a], items[b]))

# print(pairs)

# items = 'ABCDE'
# pairs = [(items[a], items[b])
#     for a in range(len(items)) for b in range(a, len(items))]
# print(pairs)

#-------------------------------------------------------------
#Set Comprehension

# a = {i*i for i in range(1,11) if i%2==0}
# print(a)

#--------------------------------------------------

#Dict Comprehension
# a = {i:i*i for i in range(1,11) if i%2==0}
# print(a)

#--------------------------------------------------
# Challenge
# Create a comprehensive list of 20 square numbers that are not divisible by 3 and 5



# a = [i*i for i in range(38) if i%3!=0 and i%5!=0]
# print(a)

# a = [i*i for i in range(100) if i%!=0 and i%5!=0]
# print(len(a[0:20]))

# a=[1,2,3,4,5,6,7,8,9,10]
# print(a[0:9])
# print(a[9])

# print([ str(n) if n > 3 
# else 'ONE' if n == 1
# else 'NA'
# for n in range(6)])	## if n > 3, return str(n)
#------------------------------------------------------------

#Generator

a=(n*n for n in range(10) )
# a=(n*n for n in range(1000) if n % 2 == 0)
# print(a)
# b=list(a)
# print(b)
# # b=list(a)
# b= sum(list(a))
# print(b)

# print(b[0:20])

#c= sum(b)
#b = sum(i*i for i in range(10) )
#print(c)
# b = sum(n*n for n in range(10) if n % 2 == 0)
# print(b)
#----------------------------------------
#Challenge
# Generate 10 square numbers that are not divisible by 3 and 5 using generator expression

# Print out the generated results

# b=(n*n for n in range(10) if n%3!=0 and n%5!=0 )
# print(b)
# print(list(b))

# print(list((n*n for n in range(10) if n%3!=0 and n%5!=0 )))


# c=list(b)[0:10]
# print(c)
# print(len(c[0:10]))





#-------------------------------------------------------
#Generator Expression for Tuple

# a=list( (n, n**2) for n in range(10) )
# b=list( (n, n**2) for n in range(10)  if  n%2 == 0)
# print(a)
# print(b)

#---------------------------------------------
#Generator Function

# def range_sq(n):
# 	for x in range(n):
# 		yield x ** 2  
# print(range_sq(10))
# print(list(range_sq(10)))

# for i in range_sq(10):
# 	print(i)




#yield from
# def range_sq(n):
#     yield from (i ** 2 for i in range(n))

# for i in range_sq(10):
#  	print(i)

#-----------------------------------------------------

#Challenge: Geometric Progression

# def geo(a,r,n):
#     for x in range(n):
#         yield a*(r**x)

# def geo(a,r,n):
#     yield from(a*(r**x) for x in range(n))

# for i in geo(1,2,5):
#  	print(i)


