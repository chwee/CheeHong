#Set----------------


#Change element in set
#s = set([2,3,4,5,6,1])

#do not support index
#s[0]=0

#set add element
# s.add(7)
# print(s)

#set do not add duplicate element
# s.add(2)
# print(s)


#set update
# s.update([7,8,9])
# print(s)
# s.update([7,8,9],{10,11,12})
# print(s)

#---------------------------------------
#Remove element from set
# The only difference between the two is that, while using discard() 
# if the item does not exist in the set, it remains unchanged. 
# But remove() will raise an error in such condition. 

# s.discard(1)
# print(s)
# s.remove(1)
# print(s)

#----------------------------------------------------------



#------------------------------------
# Difference of A and B (A - B) is a set of elements that are only in A but not in B. 
# Similarly, B - A is a set of element in B but not in A.
#  Difference is performed using - operator. 
#  Same can be accomplished using the method difference().


# s = set([1, 2, 3, 4, 5,5,5])
# x= set([4,5,6,7,8])
# print(s)
# # print(len(s))	 			
# # print(x in s)	 		
# # print(x not in s)	 		
# # print(x.issubset(s))			#s <= t		
# # print(s.issuperset(x))			#s >= t		
# # print(x.union(s))				#s | t	
# # print(x.intersection(s))		#s & t	
# print(x.difference(s))			#s - t	

#--------------------------------------------------------
#new set with elements in either s or t but not both
# s1 = set([1, 2, 3, 4, 5])
# u= set([4,5,6,7,8])
# z=s1.symmetric_difference(u)
# print(z)

# s={1,2,3,4,6}
# print(s)

