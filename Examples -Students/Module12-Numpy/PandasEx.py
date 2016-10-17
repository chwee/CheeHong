#Pandas

import pandas as pd
import numpy as np

#Series ----------------------------------------------

# s = pd.Series([1,3,5,6,2,4,6,2])
# print(s)
#-------------------------------------------

#Create Series from NP Array
# s = pd.Series(np.random.randn(100))
# print(s)
# print(s[97])

#-----------------------------------------------------
#Create Series with index
# s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(s)
# print(s[2])

#Create Series From Dictionary
#s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7})
# print(s)

#------------------------------------------------------
#Select Data
#View Series Data

#s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7})
# print(s)
# #print(s.head())		#first 5 rows

# print(s.head(10))	    #first 10 rows

#print(s.tail())	    #last 5 rows
#print(s.tail(10))		#last 10 rows

#----------------------------------
#Show Index & Values 
# s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7})

# print(s.index)			#show the indexes
# print(s.values)		        #show the values

#---------------------------------------------------------
#Selecting Data
# s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7})

# print(s[2])				# select item 2
# print(s[[2, 5, 2]])	#select item 2, 5 and 2
# print(s[3:6])			#slice items 3 to 6

#--------------------------------------------------
#series attrubute
# s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6, 'g':7})

# print(len(s))		# Number of elements in a Series
# print(s.shape)		# Dimensionality of a Series
# print(s.count())	#  Number of elements excl. NaN
# print(s.unique())	# List all unique elements
# print(s.value_counts()) # List all unique values and their counts

#------------------------------------------------------
#Series Arithmetic

# a = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# b = pd.Series([1, 1, 1, 1], index=['a', 'b', 'c', 'd'])
# print(a + b)		# different from Python list
# print(a - b)
# print(a * b)
# print(a/b)
#-----------------------------------------------------------

#DataFrame
#What is DataFrame?
#$DataFrame is similar to a spreadsheet in Excel

#Creating Data Frame
#Create DF from Python List
# df = pd.DataFrame([[1,1],[2,2]])
# print(df)


#Create DF from NP Array
# df = pd.DataFrame(np.random.randn(2,2))
# print(df)

#Create DF From Series
# df = pd.DataFrame([pd.Series(np.arange(10, 15)), pd.Series(np.arange(15, 20))])
# print(df)
# print(df.shape)

#Create DF With Columns
# df = pd.DataFrame([[1,2],[3,4]],columns=['height','weight'])
# print(df)

#Create DF With Columns & Index
# df = pd.DataFrame([[1,2],[3,4]],index=[1,2],columns = ['height','weight'])
# print(df)

#Create DF From Series & Dict
#????????
# df1 = pd.Series(np.arange(1, 6, 1))
# df2 = pd.Series(np.arange(6, 11, 1))
# pd.DataFrame({'c1': df1, 'c2': df2})
# print(pd)

#Create Data Frame with Date
# dates = pd.date_range('20130101', periods=6)
# df = pd.DataFrame(np.random.randn(6,4), index=dates)
# print(df)

#---------------------------------------

#Dataframe Attributes
# df = pd.DataFrame([[1,2],[3,4]],columns=['height','weight'])
# print(df)

# print(df.shape)		#Dimensionality of a DF
# print(df.columns)	    #columns of a DF
# print(df.index)	    # index of a DF
# print(df.values)		#values of a DF

#-------------------------------------------------------------
#DataFrame Arithmetic

# df1 = pd.DataFrame([[1,2],[3,4]],index=[1,2],columns=['a','b'])
# df2 = pd.DataFrame([[4,3],[2,1]],index=[2,1],columns=['b','a'])

# print(df1)
# print(df2)

#print(df1 + df2)	# different from Python list
# print(df1 - df2)
#print(df1 * df2)
# print(df1/df2)

#-------------------------------------------------------
#Import Data

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#Create dataframe (that we will be importing)
# raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#         'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
#         'age': [42, 52, 36, 24, 73],
#         'preTestScore': [4, 24, 31, ".", "."],
#         'postTestScore': ["25,000", "94,000", 57, 62, 70]}
# df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
# #print(df)

#Save dataframe as csv in the working director
#df.to_csv('example.csv')

#Load a csv
# df = pd.read_csv('example.csv')
# print(df)

#Load a csv with no headers
# df = pd.read_csv('example.csv', header=None)
# print(df)

#Load a csv while specifying column names
# df = pd.read_csv('example.csv', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df)

#Load a csv with setting the index column to UID
# df = pd.read_csv('example.csv', index_col='UID', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df)


#Load a csv while setting the index columns to First Name
#and Last Name
# df = pd.read_csv('example.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df)

#Load a csv while specifying "." as missing values
# df = pd.read_csv('example.csv', na_values=['.'])
# print(df)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#--------------------------------------------------------
#View Import Data

#Load a csv
# df = pd.read_csv('example.csv')
# print(df)

# print(df.head())
# print(df.head(3))

# print(df.tail())
#print(df.tail(3))

#-------------------------------------------------------------
#View Index & Values
#Load a csv
# df = pd.read_csv('example.csv')
# # print(df)

# print(df.index)
# print(df.values)

#-------------------------------------------------------------
#Selecting Columns

#Load a csv
#df = pd.read_csv('example.csv')
#print(df)

# print(df[[1]])
# print(df['first_name'])

# print(df[[1,2]])
# print(df[['first_name','age']])

# print(df[[1,2]].head(2))
# print(df[['first_name','age']].head(2))

#----------------------------------------------------
#Selecting Rows

#Load a csv
# df = pd.read_csv('example.csv')
# print(df)

#Display 3 rows
#print(df[:3])

#loc
#Now, let’s extract a subset of the dataframe. 
#Here is the general syntax rule to subset portions of a 
#dataframe:
#df2.loc[startrow:endrow,startcolumn:endcolumn]
#example
#print(df.loc[1:3, 'first_name':'age'])

#iloc
#Now, sometimes, you don’t have row or column labels. 
#In such case you will have to rely on position based 
#indexing which is implemented with iloc instead of loc:
#df2.iloc[0:3,0:4]
#Example display row inform 
#print(df.iloc[1:4, 2:])

#Selecting Rows by ix
#print(df.ix[1:4, 'first_name':'age'])


# loc works on labels in the index.
# iloc works on the positions in the index (so it only takes integers).
# ix usually tries to behave like loc but falls back to behaving like iloc if the label is not in the index.

#Selecting Rows by Boolean Ops
#display age >40
#print(df[df.age >40])

#-------------------------------------------------------------

#Selecting Scalar

# at: get scalar values. It's a very fast loc
# iat: Get scalar values. It's a very fast iloc

#Load a csv
# df = pd.read_csv('example.csv')
# print(df)

#print(df.at[['first_name','age', 'preTestScore']])

#print(df.iat[:, :])

#-----------------------------------------------------------


# from pandas.io.data import DataReader
# from datetime import datetime

# ibm = DataReader('IBM',  'yahoo', datetime(2000,1,1), datetime(2012,1,1))
# print(ibm)
# #print(ibm['Adj Close'])