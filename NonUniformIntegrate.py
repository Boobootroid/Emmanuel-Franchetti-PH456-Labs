# Emmanuel Franchetti, 24/2/22
# Lab 2, Task 5: Metropolis method integration

# Pass in expression as string, independent variables as list of strings, limits
# as list of pairs of numbers (lower then upper) and the number of samples
import numpy as np
import math as mth
import sys

def NonUniformIntegrate(expression, independentVars, lims, numSamples, PDF, metDelta, metStart):      
    ### SET CLASSES
    ## Create Class for function to be integrated
    class Function:
        ## Class has three properties, function, independent variables & PDF
        def __init__(self, function, independentVariables, probDistFunc):
            self.func = function # String
            self.indVars = independentVariables # List of variable names as strings
            self.pdf = probDistFunc # String
            
        ## Evaluate function (or PDF) at passed in value
        # inputVars must be list of numbers
        def f(self, inputVars, ftype=None):
            # if ftype is None, evaluates function as normal
            while ftype ==None:
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
            # Check if function is PDF
            if ftype == 'PDF':
                # Special case if PDF is a constant
                if self.indVars == ['']:
                    p = eval(self.pdf)
                    return p
                # Check that the correct amount of variables have been passed in
                if len(inputVars) == len(self.indVars):
                    # Set independent variables
                    for i in range(len(inputVars)):
                        name = self.indVars[i] # Name of Variable
                        num = inputVars[i] # value of passed in variable
                        exec("%s = %f" % (name, num)) # Dynamically assign independent variables
                    # Evaluate pdf at passed in variables
                    p = eval(self.pdf)
                    return p # return pdf value
            else:   
                print("ERROR: FUNCTION TYPE UNRECOGNISED")
                sys.exit()



    ### PARAMETERS
    # Define function and its variables. variables must be passed as list of strings   
    fun = Function(expression,independentVars, PDF)
    # Check that there is the correct number of limits per variable
    if len(lims) != len(fun.indVars)*2:
        print("ERROR: INCORRECT NUMBER OF LIMITS SET")
        sys.exit()    

    loopLimit = 10**7 # Stops program after this many loops incase of infinite loop

    ### MAIN
    rng = np.random.default_rng() # pick PRNG
    samplesX = []    
    delta = metDelta
    numLoops = 0
    # 0. Start with an initial state, xi.
    xi = metStart
    # Loop until integral can sum over numSample values, or until a limit is reached
    while len(samplesX)< numSamples and numLoops < loopLimit:
        # 1. Choose a new trial position xtrial = xi + δi where δi is a random number in the interval [−δ, δ].
        xtrial = xi+((2*delta)*rng.random()-delta)
        # 2. Calculate w = p(xtrial)/p(xi).
        pxtrial = fun.f([xtrial], 'PDF') 
        pxi = fun.f([xi], 'PDF') 
        w = pxtrial/pxi
        # 3. If w > 1, accept the change and set xi+1 = xtrial.
        if w>=1:
            xi = xtrial
            samplesX += [xi]
        # 4. If w < 1, generate a random number r in the range [0, 1].
        # 5. if r<= w, accept the change and set xi+1 = xtrial.
        if w<1 and rng.random() <= w:
            xi = xtrial
            samplesX += [xi]
        # 6. Otherwise reject the new position set xi+1 = xi.
        # 7. Set i ← i + 1, and return to step 1.
        numLoops +=1
        if len(samplesX) == numSamples-1:
            print(str(numLoops-len(samplesX))+' samples rejected')
            
    # use random samples to find function samples
    fByP = []
    for i in range(numSamples):
        sampleF = fun.f([samplesX[i]])
        sampleP = fun.f([samplesX[i]], 'PDF')
        fByP += [sampleF/sampleP]
    # Calculate integral
    integral = (1/numSamples)*(sum(fByP)) 
    
    return integral
    
    
    
    
