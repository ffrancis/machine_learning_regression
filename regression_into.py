# Computing regression parameters

import numpy as np


X = [0, 1, 2, 3, 4]
Y = [1, 3, 7, 13, 21]

#print X
#print Y

#We want the line that "best fits" this data set as measured by residual sum of squares -- the simple linear regression cost. We have a closed form solution that involves the following terms:

#The number of data points (N)
#The sum (or mean) of the Ys
#The sum (or mean) of the Xs
#The sum (or mean) of the product of the Xs and the Ys
#The sum (or mean) of the Xs squared


mean_Y  = np.mean(Y)
mean_X  = np.mean(X)
mean_XY    = np.mean([x*y for x,y in zip(X, Y)])
mean_Xsq    = np.mean([x*x for x in list(X)])


print mean_Y, mean_X, mean_XY, mean_Xsq


#Then once we have calculated all of these terms, we can use the formulas to compute the slope and intercept.
