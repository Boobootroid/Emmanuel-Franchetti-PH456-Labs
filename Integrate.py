# Emmanuel Franchetti, 24/2/22
# Lab 2, Task 1: Monte carlo integration, returns value of integral with 
# standard deviation

# Pass in expression as string, independent variables as list of strings, limits
# as list of pairs of numbers (lower then upper) and the number of samples
import numpy as np
import math as mth
import sys

def Integrate(expression, independentVars, lims, numSamples):      
    ### SET CLASSES
    ## Create Class for function to be integrated
    class Function:
        ## Class has two properties, function and independent variables
        def __init__(self, function, independentVariables):
            self.func = function # String
            self.indVars = independentVariables # List of variable names as strings
            
        ## Evaluate function at passed in value
        # inputVars must be list of numbers
        def f(self, inputVars):
            # Special case if function is a constant
            if self.indVars == ['']:
                f = eval(self.func)
                return f # return function value, independent of passed in value
            # Check that the correct amount of variables have been passed in
            if len(inputVars) == len(self.indVars):
                # Set independent variables
                for i in range(len(inputVars)):
                    name = self.indVars[i] # Name of Variable
                    num = inputVars[i] # value of passed in variable
                    exec("%s = %f" % (name, num)) # Dynamically assign independent variables
                # Evaluate function at passed in variables
                f = eval(self.func)
                return f # return function value
            else:
                print("ERROR: INCORRECT NUMBER OF INDEPENDENT VARIABLES PASSED IN")
                sys.exit()
           
            
         
    ### PARAMETERS
    # Define function and its variables. variables must be passed as list of strings   
    fun = Function(expression,independentVars)
    # Check that there is the correct number of limits per variable
    if len(lims) != len(fun.indVars)*2:
        print("ERROR: INCORRECT NUMBER OF LIMITS SET")
        sys.exit()    

    
    
    ### MAIN
    rng = np.random.default_rng() # pick PRNG
    ## Find average value of function within limits
    samples = np.zeros(numSamples,float)
    for i in range(numSamples):  
        rands = np.zeros(len(fun.indVars),float) # empty array for random sample of independent variables
        for j in range(len(fun.indVars)):
            # Pick limits for one independent variable
            lowerLim = lims[2*j]
            upperLim = lims[2*j+1]
            # Picks a random number within integral limits for each independent variable per sample
            rands[j] = (upperLim-lowerLim)*rng.random()+lowerLim     
        samples[i] = fun.f(rands) # Pass random numbers into function to get random samples
    
    
    ## Calculate Integral
    domain = 1
    for i in range(len(fun.indVars)): # Extract Domain of integral as one constant
        lowerLim = lims[2*i]
        upperLim = lims[2*i+1]
        domain = domain*(upperLim-lowerLim)
    integral = (domain/numSamples)*(np.sum(samples)) 
    
    #Calculate Standard Deviation for each sample
    stdDev = mth.sqrt((1/numSamples)*((np.sum(np.square(samples))/numSamples)-((1/numSamples)*np.sum(samples))**2)) # sigma = sqrt(1/n*(<f>^2-<f^2>))
    
    return integral, stdDev





