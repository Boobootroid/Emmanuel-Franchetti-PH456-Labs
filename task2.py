
### Emmanuel Franchetti PH456 2022
### Task 2,3
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator, MT19937
from scipy.stats import sem

### PARAMETERS
N=250 # Number of particles in box
time = 10000 # total time of simulation
setTime = 1000 # 'Settling' time for particles to reach equilibrium

### MAIN PCG64
box = np.full((N,1),-1) # 1 corresponds to RHS, -1 Corresponds to LHS
boxcount = np.full(time,0)
boxcountright = np.full(time,0)

rng = np.random.default_rng(4)
for t in range(time):
    rand = rng.integers(0, N-1) #random number from 0 to N-1
    box[rand] = box[rand]*(-1)
    boxcount[t] = np.count_nonzero(box==-1)
    boxcountright[t] = np.count_nonzero(box==1)
    boxmean = round(np.mean(boxcount[setTime:time]),2)
    boxsem = round(sem(boxcount[setTime:time]),2)
    
fig2, ax2 = plt.subplots()
plt.scatter(range(time), boxcount, marker = "o", s=0.5, label="LHS", c="r")
plt.scatter(range(time), boxcountright, marker = "o", s=0.5, label="RHS", c="b")   
plt.title('Time evolution of '+str(N)+' particles in box @ seed=4')
plt.legend(loc='upper right')
ax2.set_ylabel('# of particles')
ax2.set_xlabel('Time')
ax2.set_ylim(0)
ax2.set_xlim(0)

fig, ax = plt.subplots()
plt.scatter(range(time), boxcount, marker = "o", s=0.5, label="PCG64", c="r")
ax.hlines(boxmean,setTime,time,linestyle='dashed',colors="Pink",label="Mean="+str(boxmean)+"+-"+str(boxsem))

### MAIN MT19937
#Reset variables
box = np.full((N,1),-1) # 1 corresponds to RHS, -1 Corresponds to LHS
boxcount = np.full(time,0)

rng = Generator(MT19937(4))
for t in range(time):
    rand = rng.integers(0, N-1) #random number from 0 to N-1
    box[rand] = box[rand]*(-1)
    boxcount[t] = np.count_nonzero(box==-1)
    boxmean = round(np.mean(boxcount[setTime:time]),2)
    boxsem = round(sem(boxcount[setTime:time]),2)
    
plt.scatter(range(time), boxcount, marker = "o", s=0.5, label="MT19937", c="b")
ax.hlines(boxmean,setTime,time,linestyle='dashed',colors="Cyan",label="Mean="+str(boxmean)+"+-"+str(boxsem))

plt.title('Time evolution of '+str(N)+' particles in box @ seed=4')
plt.legend(loc='upper right')
ax.set_ylabel('# of particles in LHS')
ax.set_xlabel('Time')
ax.set_ylim(0)
ax.set_xlim(0)
plt.show()