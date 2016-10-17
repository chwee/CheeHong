
g= input("Enter here:")
grade=['A','B','C']
if g not in grade:
	print("Please enter A to C")
else:
    if g == 'A':
        print("Excellent!")
    if g == 'B':
        print('Well done!')
    if g == 'C':
        print("Good job!")
