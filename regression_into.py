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


#print mean_Y, mean_X, mean_XY, mean_Xsq


#Then once we have calculated all of these terms, we can use the formulas to compute the slope and intercept.
#numerator = (sum of X*Y) - (1/N)*((sum of X) * (sum of Y))
#denominator = (sum of X^2) - (1/N)*((sum of X) * (sum of X))

#which is the same as (after dividing numeratro and denominator by N)
#numerator = (mean of X*Y) - (mean of X)*(mean of Y)
#denominator = (mean of X^2) - (mean of X)*(mean of X)

numerator   = mean_XY - (mean_X*mean_Y)
denominator = (mean_Xsq) - (mean_X)*(mean_X)
slope       = numerator/denominator

#intercept = (mean of Y) - slope * (mean of X)
intercept = (mean_Y) - slope * (mean_X)

print "numerator = ", numerator, "denominator = ", denominator, "slope = ", slope, "intercept = ", intercept
























