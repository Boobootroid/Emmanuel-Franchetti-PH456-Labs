# Emmanuel Franchetti, 24/2/22
# Lab 2: Task 3
import Integrate
import numpy as np
import matplotlib.pyplot as plt
import math as mth

### Parameters
numSamples = 10000 # Number of samples
ro= 2

funA = "mth.sqrt(x**2+y**2+z**2)<="+str(ro) # Define function
indVarsA= ['x','y','z'] # Define independent variables
limsA = [-ro,ro,-ro,ro,-ro,ro,] # Integral Limits. Must be list of numbers, in lower and upper pairs.
answerA = 33.51 # true value of integral

funB = "mth.sqrt(x**2+y**2+z**2+a**2+b**2)<="+str(ro) # Define function
indVarsB= ['x','y','z','a','b'] # Define independent variables
limsB = [-ro,ro,-ro,ro,-ro,ro,-ro,ro,-ro,ro,]
answerB = 168.44 # true value of integral
 

#Calculate integrals
integralA = Integrate.Integrate(funA,indVarsA,limsA,numSamples)
print('3-Ball volume @ r='+str(ro)+': '+str(integralA[0]))

integralB = Integrate.Integrate(funB,indVarsB,limsB,numSamples)
print('5-Ball volume @ r='+str(ro)+': '+str(integralB[0]))
