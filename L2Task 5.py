# Emmanuel Franchetti, 01/3/22
# Lab 2: Task 5
import NonUniformIntegrate as nui
import numpy as np
import matplotlib.pyplot as plt
import math as mth

numSamples = 10000

### Part A
fx = '2*mth.exp(-x**2)'
indvar = ['x']
normalConst = '1/(2-2*mth.exp(-10))'
pdf = normalConst+'*mth.exp(-abs(x))'
lims = [-10,10]
answer = 3.5449 # true value of integral
metDelta = 2 #Step size in metropolis method, denoted by delta
metStartX = 0 # Starting point for metropolis method

integral =  nui.NonUniformIntegrate(fx,indvar,lims, numSamples, pdf, metDelta, metStartX)
perc = 100-100*abs(integral-answer)/answer 
print('Part A) Integral: '+str(integral)+', '+str(perc)+'% accurate')


### Part B
fx = '1.5*mth.sin(x)'
indvar = ['x']
normalConst = '3/(2*mth.pi)'
pdf = normalConst+'*4*(mth.pi**-2)*x*(mth.pi-x)'
lims = [0,mth.pi]
answer = 3 # True value of integral
metDelta = 1.5 #Step size in metropolis method, denoted by delta
metStartX = mth.pi/2 # Starting point for metropolis method

integral =  nui.NonUniformIntegrate(fx,indvar,lims, numSamples, pdf, metDelta, metStartX)
perc = 100-100*abs(integral-answer)/answer
print('Part B) Integral: '+str(integral)+', '+str(perc)+'% accurate')









