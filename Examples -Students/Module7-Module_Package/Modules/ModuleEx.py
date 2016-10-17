#Import modules 
#Import everything
# import math
# print(math.sin(0.5))

# #Import with abbreviation
# import math as m
# print(m.sin(0.5))
# print(m.pi)

#-----------------------------------------------
#Import a custom module
import message as myMsg
import cal 
#from cal import add
myMsg.echoMsg("Test echo message")

myMsg.echoMsg2("Test echo message")

print(cal.add(10,3))
#print(add(10,3))