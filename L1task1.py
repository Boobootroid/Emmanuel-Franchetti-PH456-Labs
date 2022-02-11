
#probability of finding points within range of each other? ripleys k test?


### Emmanuel Franchetti PH456 2022
### Task 1
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import Generator, MT19937

### PARAMETERS
numrands = 2000 #Input number of random numbers
randrange = [1,100] #Input range of random numbers
seeds = [1,2] #Input starting seeds for psuedo-random number generator
shift = 5 # Shift each row in random number array for scatter plot


### MAIN
# Initialise empty 2d array with rows = # of seeds, columns = # of random numbers
pcgArray = np.empty((len(seeds),numrands),int)
mtArray = np.zeros((len(seeds),numrands),int)

# Generate set of random numbers for each seed specified
for i in range(len(seeds)):
    # Input seed for PCG64 generator
    rng = np.random.default_rng(seeds[i])   
    pcgArray[i] = rng.integers(randrange[0], randrange[1], size=(numrands)) 

# Generate set of random numbers for each seed specified
for i in range(len(seeds)):
    # Input seed for MT19937 generator
    rng = Generator(MT19937(seeds[i]))   
    mtArray[i] = rng.integers(randrange[0], randrange[1], size=(numrands)) 
      


# make new figure for each seed
for i in range(len(seeds)):
    
    # For PCG
    x= pcgArray[i,0:numrands-shift] # normal array minus shift elements
    y= pcgArray[i,shift:numrands] # shifted array ignoring first shift elements
       
    # open figure
    fig,ax = plt.subplots()
    plt.scatter(x,y, s=0.5)
    plt.title('PCG64, '+str(numrands)+' Points, Seed = '+str(seeds[i]))
    ax.set_ylabel('U[n+'+str(shift)+']')
    ax.set_xlabel('Sequence U[n]')
    
    # For MT   
    x= mtArray[i,0:numrands-shift] # normal array minus shift elements
    y= mtArray[i,shift:numrands] # shifted array ignoring first shift elements
    
    # open figure
    fig,ax = plt.subplots()
    plt.scatter(x,y, s=0.5)
    plt.title('MT19937, '+str(numrands)+' Points, Seed = '+str(seeds[i]))
    ax.set_ylabel('U[n+'+str(shift)+']')
    ax.set_xlabel('Sequence U[n]')


#autocorrelations
mtautocorr = np.correlate(mtArray[0,:],mtArray[0,:], 'same')
pcgautocorr = np.correlate(pcgArray[0,:],pcgArray[0,:], 'same')
#Cross Correlation
crosscorr = np.correlate(pcgArray[0,:],mtArray[0,:], 'same') 


# Plotting correlations
fig, ax = plt.subplots()
ax.plot(range(numrands), mtautocorr)
plt.title('Auto Correlation for MT19937 Sequence @ Seed =1')
ax.set_ylabel('Correlation')
ax.set_xlabel('Shift')
plt.show()
fig, ax = plt.subplots()
ax.plot(range(numrands), pcgautocorr)
plt.title('Auto Correlation for PCG64 Sequence @ Seed =1')
ax.set_ylabel('Correlation')
ax.set_xlabel('Shift')
plt.show()
fig, ax = plt.subplots()
ax.plot(range(numrands), crosscorr)
plt.title('Cross Correlation @ Seed =1')
ax.set_ylabel('Correlation')
ax.set_xlabel('Shift')
plt.show()


####




# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.title('Random Numbers')
# ax.set_ylabel('Rnd Number')
# ax.set_xlabel('Position in Array')
# plt.show()

# result = np.correlate(x,x, mode='same')
# print(result)

# fig, ax = plt.subplots()
# ax.plot(x, result)
# plt.title('Correlate result')
# ax.set_ylabel('')
# ax.set_xlabel('')
# plt.show()



# # open figure
# fig,ax = plt.subplots()



# plt.scatter(pcgArray[0,:],pcgArray[1,:], s=0.1)
# plt.title('PGC64')
# ax.set_ylabel('Seed=2')
# ax.set_xlabel('Seed=1')






