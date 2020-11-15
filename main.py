import matplotlib.pyplot as plt 
import numpy as np 

def magnetisation( spins ) :
  mag = 0
  # Your code to calculate the magnetisation goes here
  
  return mag
  
def hamiltonian( spins, H ) :
  eng = 0
  # Your code to calculate the energy goes here
  
  return eng
  
# Create a list of the posssible values the magnetisation can take
magnetisations = 17*[0]
for i in range(17) : magnetisations[i] = -8+i

# Create a list that will hold the probability of having a particular value for the 
# magnetisation
probabilities = 17*[0]
# Your code to do the loop over all the microstates and to compute the sum of the unormalized
# probabilities for the states with each particular magnetisation value as well as the 
# canonical partition function goes here
T, H, Z = 1.5, 0.2, 0


# Normalize the probabilities by dividing by the partition function
for i in range(17) : probabilities[i] = probabilities[i] / Z
  
# This will plot the energies of the configurations against their numerical indexes. 
plt.bar( magnetisations, probabilities, width=0.1 )
plt.xlabel("magnetisation")
plt.ylabel("probability")
plt.savefig( "marginal_distribtuion.png" )
