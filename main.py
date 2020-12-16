import matplotlib.pyplot as plt 
import numpy as np 

def magnetisation( spins ) :
  mag = 0
  # Your code to calculate the magnetisation goes here
  mag = sum(spins)
  return mag
  
def hamiltonian( spins, H ) :
  eng = 0
  # Your code to calculate the energy goes here
  eng = - spins[0]*spins[-1] - H*spins[0]
  for i in range(1,len(spins)) : eng = eng - spins[i-1]*spins[i] - H*spins[i]
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
for index in range(2**8) :
  spins, ind = 8*[0], index
  # Your code to convert the integer index to the corresponding spin coordinates goes here
  for i in range(8) :
      spins[i] = np.floor( index / 2**(7-i) )
      index = index - spins[i]*(2**(7-i))
      if spins[i]==0 : spins[i] = -1
  nbin = int( magnetisation(spins) ) + 8
  bweight = np.exp( -hamiltonian(spins,H)  / T ) 
  probabilities[nbin] = probabilities[nbin] + bweight
  Z = Z + bweight

# Normalize the probabilities by dividing by the partition function
for i in range(17) : probabilities[i] = probabilities[i] / Z
  
# This will plot the energies of the configurations against their numerical indexes. 
plt.bar( magnetisations, probabilities, width=0.1 )
plt.xlabel("magnetisation")
plt.ylabel("probability")
plt.savefig( "marginal_distribtuion.png" )
