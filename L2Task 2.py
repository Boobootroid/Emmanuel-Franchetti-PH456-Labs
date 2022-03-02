# Emmanuel Franchetti, 24/2/22
# Lab 2: Task 2
import Integrate
import numpy as np
import matplotlib.pyplot as plt

numSamples = 10000 # Number of samples
### Part a)
funA = "2" # Define function
indVarsA= [''] # Define independent variables
limsA = [0,1] # Integral Limits. Must be list of numbers, in lower and upper pairs.
answerA = 2 # true value of integral
 
integralA = Integrate.Integrate(funA,indVarsA,limsA,numSamples) # first value is integral value, second is std deviation
### Part b)
funB = "-x" # Define function
indVarsB= ['x'] # Define independent variables
limsB = [0,1] # Integral Limits. Must be list of numbers, in lower and upper pairs.
answerB = -0.5 # true value of integral
 
integralB = Integrate.Integrate(funB,indVarsB,limsB,numSamples) # first value is integral value, second is std deviation
### Part c)
funC = "x**2" # Define function
indVarsC= ['x'] # Define independent variables
limsC = [-2,2] # Integral Limits. Must be list of numbers, in lower and upper pairs.
answerC = 16/3 # true value of integral

integralC = Integrate.Integrate(funC,indVarsC,limsC,numSamples) # first value is integral value, second is std deviation
### Part d)
funD = "x*y+x" # Define function
indVarsD= ['x','y'] # Define independent variables
limsD = [0,1,0,1] # Integral Limits. Must be list of numbers, in lower and upper pairs.
answerD = 3/4 # true value of integral
 
integralD = Integrate.Integrate(funD,indVarsD,limsD,numSamples) # first value is integral value, second is std deviation

### Evaluating effect of increase in sampling number on integral accuracy on part B
stepSize = 100
j=0
accuracy = np.zeros((numSamples//stepSize),float)
stdDevs = np.zeros((numSamples//stepSize),float)
# Loops from stepSize to the number of samples set at begining of program
for i in range(stepSize,numSamples+stepSize,stepSize):
    print('Integrated with '+str(i)+' samples')
    integral = Integrate.Integrate(funB,indVarsB,limsB,i)
    accuracy[j] = 100-abs((100*(abs(answerB - integral[0])/answerB))) # Accuracy as a percentage of the answer
    stdDevs[j] = abs(integral[1]/answerB)
    j=j+1


## Plotting results
fig, ax = plt.subplots()
ax.plot(range(stepSize,numSamples+stepSize,stepSize), accuracy)
plt.title('Accuracy of random integral with increasing sample size')
ax.set_ylabel('Accuracy[% of true answer]')
ax.set_xlabel('Number of random samples')
plt.show()

fig, ax = plt.subplots()
ax.plot(range(stepSize,numSamples+stepSize,stepSize), stdDevs)
plt.title('Standard Deviation of random integral with increasing sample size')
ax.set_ylabel('Standard Deviation [% of true answer]')
ax.set_xlabel('Number of random samples')
plt.show()









