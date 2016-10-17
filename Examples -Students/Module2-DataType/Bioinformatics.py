
# #Counting Letters in DNA Strings
# def count_v12(dna, base):
#      return dna.count(base)

# dna = 'ATGCGGACCTAT'
# base = 'C'
# n = count_v12(dna, base)

# # # or (new) format string syntax
# print('{base} appears {n} times in {dna}'.format(
#      base=base, n=n, dna=dna))
#--------------------------------------------------------------

# #Extracting Indices of base characters 

# # Extracting Indices of base

#method 1  comprehension
# def count_v11(dna, base):
#      return [i for i in range(len(dna)) if dna[i] == base]

#method 2
# def count_v11(dna, base):
# 	info=[]
# 	for  i in range(len(dna)):
# 		if dna[i] == base:
# 			info.append(i)
# 	return info


# dna = 'ATGCGGACCTAT'
# base = 'C'
# n = count_v11(dna, base)
# print(n)

# for i in n:
#  	print(dna[i])
#------------------------------------------------------