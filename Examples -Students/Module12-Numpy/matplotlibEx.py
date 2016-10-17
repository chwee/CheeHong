import numpy as np
import sys
import matplotlib.pyplot as plt

#Plot curve
x = np.linspace(0,4*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()

#Marker
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# plt.plot(x,y)
# plt.plot(x,y,'-^') # adding triangle markers
# plt.plot(x,y,'-o') # adding circle markers
# plt.show()


#Line Style
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# plt.plot(x,y,'--')
# plt.show()

#color
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# plt.plot(x,y,'g')
# plt.show()

#grid line
x = np.linspace(0,4*np.pi,100)
y = np.sin(x)
plt.plot(x,y,'g')
plt.grid()
plt.show()

#label
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# plt.plot(x,y,'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('A sine curve')
# plt.axis([0,4*np.pi,-2,2])
# plt.show()


#Overlay Plots and Legend
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# y1= np.cos(x)
# plt.plot(x,y,'c',label='y=sin(x)')
# plt.plot(x,y1,'y',label='y=cos(x)')
# plt.legend(loc='upper left')
# plt.show()



#subplot
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# y1= np.cos(x)
# plt.subplot(2,1,1)
# plt.plot(x,y,'c',label='y=sin(x)')
# plt.legend(loc='upper left')
# plt.subplot(2,1,2)
# plt.plot(x,y1,'y',label='y=cos(x)')
# plt.legend(loc='upper left')
# plt.show()

#-------------------------------
#chanllenge

# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# y2 = np.cos(x)
# y3 = np.sin(x) * np.cos(x)
# y4 = np.sin(x)- np.cos(x)

# plt.subplot(2,2,1)
# plt.plot(x,y,'r',label='y=sin(x)')
# plt.legend(loc='upper left')
# plt.subplot(2,2,2)
# plt.plot(x,y2,'y',label='y=cos(x)')
# plt.legend(loc='upper left')
# plt.subplot(2,2,3)
# plt.plot(x,y3,'g',label='y=sin(x) * cos(x)')
# plt.legend(loc='upper left')
# plt.subplot(2,2,4)
# plt.plot(x,y4,'b',label='y=cos(x) - sin(x)')
# plt.legend(loc='upper left')
# plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
# plt.show()

#---------------------------------
# x = np.linspace(0,4*np.pi,100)
# y = np.sin(x)
# y2 = np.cos(x)
# y3 = np.sin(x) * np.cos(x)
# y4 = np.sin(x)- np.cos(x)

# plt.subplot(2,2,1)
# plt.plot(x,y,'r')
# plt.subplot(2,2,2)
# plt.plot(x,y2,'y')
# plt.subplot(2,2,3)
# plt.plot(x,y3,'g')
# plt.subplot(2,2,4)
# plt.plot(x,y4,'b')

# plt.legend(loc='upper left')
# plt.show()



#-----------------------------------------------------
#Examples
# def plot5():
#     data = [ (1, 0), (2, 0.1 ), (3, 1.1), (4, 1.2), (5, 2.3), 
#                 (6, 3.5), (7, 5.8) ]
#     X = [ x for (x,y) in data ]
#     Y = [ y for (x,y) in data ]
#     #print X
#     #print Y
#     plt.plot( X, Y, ':rs' )
#     plt.axis( [0, 8, 0, 6])
#     plt.xlabel( "X values" )
#     plt.ylabel( "Y values" )
#     plt.show()

# plot5()


#------------------------------------------------------
# #Scatter Plot
# x = np.arange(1, 51)
# print(x)
# y = np.random.rand(50) 
# print(y)

# plt.scatter(x,y)
# plt.show()
#--------------------------------------------------
#Bar Plot
data = [ ("data1", 34), ("data2", 22),
        ("data3", 11), ( "data4", 28),
        ("data5", 57), ( "data6", 39),
        ("data7", 23), ( "data8", 98)]
N = len( data )
x = np.arange(1, N+1)
y = [ num for (s, num) in data ]
labels = [ s for (s, num) in data ]
width = 1
bar1 = plt.bar( x, y, width, color="y" )
plt.ylabel( 'Intensity' )
plt.xticks(x + width/2.0, labels )
plt.show()

#------------------------------------------
#Contour Plot
# x = np.linspace(-1,1,255)
# y = np.linspace(-2,2,300)
# X, Y = np.meshgrid(x, y)
# z = np.sin(X)*np.cos(Y)
# plt.contour(X,Y,z,255)
# plt.show()
#-------------------------------------

#Hisotgram
# import matplotlib.pyplot as plt
# import numpy as np
# gaussian_numbers = np.random.normal(size=10000)
# print(gaussian_numbers)
# plt.hist(gaussian_numbers)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


#----------------------------------------------
# #Pie chart
# print (sys.version)
# x = np.linspace(0,4*np.pi,10)
# plt.pie(x)
# plt.show()