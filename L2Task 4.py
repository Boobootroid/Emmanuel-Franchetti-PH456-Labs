# Emmanuel Franchetti, 24/2/22
# Lab 2: Task 4
import Integrate
import numpy as np
import matplotlib.pyplot as plt
import math as mth

### Parameters
numSamples = 100000 # Number of samples

# Breaking funciton into components 
a = 'np.array([ax,ay,az])' #Define vectors
b = 'np.array([bx,by,bz])'
c = 'np.array([cx,cy,cz])'
summation = '('+a+'+'+b+')' # vector operations
dot = summation+'@'+c

function = '1/(abs('+dot+'))' # final function
indVars= ['ax','ay','az','bx','by','bz','cx','cy','cz'] # Define independent variables
lims = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,] # Integral Limits. Must be list of numbers, in lower and upper pairs.

# #Calculate integral
integral = Integrate.Integrate(function ,indVars,lims,numSamples)
print('Integral: '+str(integral[0]))


















