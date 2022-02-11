### Emmanuel Franchetti PH456 2022
### Task 4
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem

### PARAMETERS
numbers= [100,500,1000] # Number of particles in box
time = 10000 # total time of simulation
bias = [50,75,90] # percentage chance of particle moving left to right
setTime= 2000 # Time for box to settle to equilibrium


### MAIN 
boxcount = np.full((time,len(bias)),0)
boxcountright = np.full((time,len(bias)),0)
boxdeviation= np.full(((time-setTime),len(bias)),0)
rng = np.random.default_rng(5)

#initialise empty 2d array of means & std deviation for each N for each bias
boxmean=np.full((len(bias),len(numbers)),0) 
boxsem=np.full((len(bias),len(numbers)),0)

#Loop through each N, each bias and then each tick. create a new box for each bias
for n in range(len(numbers)):
    for b in range(len(bias)):
        # Create Box
        box = np.full((numbers[n],1),-1) # 1 corresponds to RHS, -1 Corresponds to LHS
        for t in range(time):
            randPart = rng.integers(0, numbers[n]-1) #draws random particle in box
            randChance = rng.integers(0,100)#draws random percentage chance
            
            # while particle is on left and cant go right, or vice versa, draw again
            while box[randPart] == -1 and randChance >= bias[b] or box[randPart] == 1 and randChance <= bias[b]:
                randPart = rng.integers(0, numbers[n]-1) #random number from 0 to N-1
                randChance = rng.integers(1,100)#random percentage chance
                
            # If random particle is on left, has bias% chance to move right
            if box[randPart] == -1 and randChance <= bias[b]:
                    box[randPart] = box[randPart]*(-1)
            # Particle is on Right and has 100-bias% chance to move left
            elif randChance > bias[b]:
                box[randPart] = box[randPart]*(-1)       
            boxcount[t,b] = np.count_nonzero(box==-1)#counts all particles on LHS                  
            boxcountright[t,b] = np.count_nonzero(box==1)
    #Calulate mean value after initial setling down period, with standard error in mean
    for b in range(len(bias)):
        boxmean[b,n] = np.mean(boxcount[setTime:time,b], dtype=np.float64)
        boxsem[b,n] = sem(boxcount[setTime:time,b])
        # Calculate deviation from mean at each tick after equilibrium
        for t in range(time-setTime):    
            boxdeviation[t,b] = boxcount[t+setTime,b]-boxmean[b,n]
   
    
### PLOTTING
    fig1, ax1 = plt.subplots()
    plt.title('Time evolution of '+str(numbers[n])+' particles in box @ Seed=5')
    
    #plot results
    for b in range(len(bias)):
        linecolour = ["r","g","b"]
        colour =["pink","yellow","cyan"]
        ax1.scatter(range(time),boxcount[:,b],marker = "o", c=colour[b],label='Bias='+str(bias[b])+'%',s=1)
        #plot means w/ std deviation
        ax1.hlines(boxmean[b,n],setTime,time,linestyle='dashed',colors=linecolour[b],label="Mean="+str(boxmean[b,n]))
    plt.legend(loc='upper right')    
    ax1.set_ylabel('# of particles in LHS')
    ax1.set_xlabel('Time')
    ax1.set_ylim(0)
    ax1.set_xlim(0)
    plt.show()

  
    
    #plot results
    fig3, ax3 = plt.subplots()
    plt.title('Time evolution of '+str(numbers[n])+' particles in box @ 75% Bias [Seed=5]')
    ax3.scatter(range(time),boxcount[:,1],marker = "o", c="r",label='LHS',s=1)
    ax3.scatter(range(time),boxcountright[:,1],marker = "o", c="b",label='RHS',s=1)
    plt.legend(loc='upper right')    
    ax3.set_ylabel('# of particles')
    ax3.set_xlabel('Time')
    ax3.set_ylim(0)
    ax3.set_xlim(0)
    plt.show()



#Plot Deviation
fig2, ax2 = plt.subplots()  
plt.hist([boxdeviation[:,0],boxdeviation[:,1],boxdeviation[:,2]], bins='auto', label = ['N=100','N=500','N=1000'])
plt.legend(loc='upper right')
plt.title('Particle deviation from mean for 20000 ticks after settling time [Seed=5]')
ax2.set_ylabel('Occurences')
ax2.set_xlabel('Deviation from mean')
ax2.set_xticks(range(-45,45))
labels = ['']*5+['-40']+['']*9+['-30']+['']*9+['-20']+['']*9+['-10']+['']*9+['0']+['']*9+['10']+['']*9+['20']+['']*9+['30']+['']*9+['40']+['']*4
ax2.set_xticklabels(labels)

