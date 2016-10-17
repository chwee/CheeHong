import sys
print (sys.version)
# name = "Rodney Dangerfield"
# score = -1  # No respect!
# print "Hello " + name + ". Your score is " + str(score)

# a=[2,4,8,9,11,14,16]
# print(a[3:-2])

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a)

import numpy as np
sadness = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(sadness[1,2])
sadness[2] += np.array([0,1,1])
print( sadness)


