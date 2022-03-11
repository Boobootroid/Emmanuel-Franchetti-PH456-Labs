# Emmanuel Franchetti, 03/3/22
# Lab 2: Task 6
import NonUniformIntegrate as nui
import Integrate as integ
import numpy as np
import matplotlib.pyplot as plt
import math as mth


### PARAMETERS
## Part A
fxA = '2*mth.exp(-x**2)'
indvarA = ['x']
normalConstA = '1/(2-2*mth.exp(-10))'
pdfA = normalConstA+'*mth.exp(-abs(x))'
limsA = [-10,10]
answerA = 3.54491 # true value of integral
metDeltaA = 2 #Step size in metropolis method, denoted by delta
metStartXA = 0 # Starting point for metropolis method

## Part B
fxB = '1.5*mth.sin(x)'
indvarB = ['x']
normalConstB = '3/(2*mth.pi)'
pdfB = normalConstB+'*4*(mth.pi**-2)*x*(mth.pi-x)'
limsB = [0,mth.pi]
answerB = 3 # True value of integral
metDeltaB = 1.5 #Step size in metropolis method, denoted by delta
metStartXB = mth.pi/2 # Starting point for metropolis method

### MAIN
integralA = []
uniIntA = []
integralB = []
uniIntB = []
percA = []
percB = []
uniPercA = []
uniPercB = []
numSamples = []
# Do integrals for increasing sample size 
for i in range(100):
    numSamples += [(i+1)*100]
    # Find integrals
    integralA += [nui.NonUniformIntegrate(fxA,indvarA,limsA, numSamples[i], pdfA, metDeltaA, metStartXA)]
    uniIntA += [integ.Integrate(fxA,indvarA,limsA, numSamples[i])]
    integralB += [nui.NonUniformIntegrate(fxB,indvarB,limsB, numSamples[i], pdfB, metDeltaB, metStartXB)]
    uniIntB += [integ.Integrate(fxB,indvarB,limsB, numSamples[i])]
    # Percentage accuracy
    uniPercA += [100-100*abs(uniIntA[i][0]-answerA)/answerA]
    percA += [100-100*abs(integralA[i]-answerA)/answerA]
    uniPercB += [100-100*abs(uniIntB[i][0]-answerB)/answerB ]
    percB += [100-100*abs(integralB[i]-answerB)/answerB]
    print('Sample Number: '+str(numSamples[i]))

### Plots
fig, ax = plt.subplots()
ax.plot(numSamples, percA, c='r', label ='Metropolis Accuracy')
ax.plot(numSamples, uniPercA, c='b', label ='Uniform Accuracy')
plt.title('Accuracy as sample number increases, part A')
plt.legend()
ax.set_ylabel('Percentage of true answer')
ax.set_xlabel('Sample number')
plt.show()   

fig, ax = plt.subplots()
ax.plot(numSamples, percB, c='r',label ='Metropolis Accuracy')
ax.plot(numSamples, uniPercB, c='b',label ='Uniform Accuracy')
plt.title('Accuracy as sample number increases, part B')
plt.legend()
ax.set_ylabel('Percentage of true answer')
ax.set_xlabel('Sample number')
plt.show()  






