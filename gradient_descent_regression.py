# Computing regression line using gradient desent

import numpy as np
import math

X = [0, 1, 2, 3, 4]
Y = [1, 3, 7, 13, 21]



#The derivative of the cost for the intercept is the sum of the errors
#The derivative of the cost for the slope is the sum of the product of the errors and the input




### gradient descent algorithm stratergy during each step of gradient descent

#1. compute the predicted values given the current slope and intercept
#2. compute the prediction errors (prediction -Y)
#3. update the intercept:
        # - compute the derivative: sum(errors)
        # - compute the adjustment as step_size times the derivative
        # - decrease the intercept by the adjustment    
#4. update the slope:
        # - compute the derivative: sum(errors*input)
        # - compute the adjustment as step_size times the derivative
        # - decrease the slope by the adjustment



#We will need a starting value for the slope and intercept, a step_size and a tolerance

initial_intercept = 0
initial_slope = 0
step_size = 0.05
tolerance = 0.01


### first iteration
predictions = [0, 0, 0, 0, 0]
errors      = [-1, -3, -7, -13, -21]                    #  prediction errors (prediction -Y)
#update intercept
derivative_intercept  = sum(errors)                               # derivative: sum(errors)
adjustment  = step_size * derivative_intercept
new_intercept   = initial_intercept - adjustment
print new_intercept

#update slope
derivative_slope  = sum([x*y for x,y in zip(X, errors)])           # X * errors
#print derivative_slope
adjustment  = step_size * derivative_slope
new_slope   = initial_slope - adjustment
#print new_slope
magnitude = np.sqrt(np.square(derivative_intercept) + np.square(derivative_slope))
#print np.square(derivative_intercept) - np.square(derivative_slope)
print magnitude

# if magnitude > tolerance, that means that the gradient descent algorithm has not converged.
# So keep iterating with n number of such steps till the magnitude < tolerance
#print derivative_intercept, derivative_slope
























































