#dictionary-----------------------

#way to generate dictionary
# d1 = dict(a=1, b=2)
# d2 = {'a': 1, 'b': -1}
# d3 = dict(zip(['a', 'b'], [1, 2]))
# d4 = dict([('a', 1), ('b', 3)])
# d5 = dict({'b': 2, 'a': 1})

# # print(d1)
# # print(d2)
# print(d3)
# print(d4)
# # print(d5)

#--------------------------------
#update dic
#repeated key will be removed
# capitals = {'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Roman'}
# capitals2 = {'Germany': 'Berlin', 'UK': 'London', 'US': 'Washington'}

# capitals.update(capitals2)
# print(capitals)

#del 
# del capitals['France']
# print(capitals)

#key
#print('%s' % capitals.keys())

# if 'Germany' in capitals.keys():
# 	print('true')


#convert dict key into list
# newlist = list()
# for i in capitals.keys():
#     newlist.append(i)
# print(newlist)

# print(capitals['UK'])


#stop HERE BELOW AER EXTRA INFO XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#-------------------------------------------
# Write a Python script to generate and print a dictionary that contains 
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5)
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#n=int(input())
# n=5
# d = dict()

# for x in range(1,n+1):
#     d[x]=x*x

# print(d)

#-----------------------------------------------------
#Update Dictionary
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)

#------------------------------------------------------------------------------
#Del Key
# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'a' in myDict: 
#     del myDict['a']
# print(myDict)

#--------------------------------------------------------------
#sort dic by key

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))

#--------------------------------------------------------------

# dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# print(dict1)
# a=list(dict1.keys())
# b=list(dict1.values())
# print(a)
# print(b)

# print(dict1['Name'])





