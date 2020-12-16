import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_magnetisation(self):
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
               spins[j] = np.floor( num / 2**(4-j) )
               num = num - spins[j]*2**(4-j)
               if spins[j]==0 : spins[j] = -1
            self.assertTrue( magnetisation( spins )==sum(spins), "The function for evaluating the magnetisations is wrong" )
    
    def test_hamiltonian(self):
        for i in range(2**5) :
            num, spins = i, 5*[0]
            for j in range(5) :
                spins[j] = np.floor( num / 2**(4-j) )
                num = num - spins[j]*2**(4-j)
                if spins[j]==0 : spins[j] = -1
            sumspins = sum( spins )
            coup_eng = spins[0]*spins[len(spins)-1]
            for i in range(len(spins)-1) : coup_eng = coup_eng + spins[i]*spins[i+1]
            self.assertTrue( np.abs(hamiltonian( spins, 1)+coup_eng+sumspins)<1e-7, "The function for evaluating the Hamiltonian is wrong" )
            self.assertTrue( np.abs(hamiltonian( spins, -1)+coup_eng-sumspins)<1e-7, "The function for evaluating the Hamiltonian is wrong" )
            self.assertTrue( np.abs(hamiltonian( spins, 0)+coup_eng)<1e-7, "The function for evaluating the Hamiltonian is wrong" )
            self.assertTrue( np.abs(hamiltonian( spins, 2)+coup_eng+2*sumspins)<1e-7, "The function for evaluating the Hamiltonian is wrong" )
    
    def test_graph(self):
        Z, counts = 0, 17*[0]
        for i in range(2**8) :
            num, spins = i, 8*[0]
            for j in range(8) :
                spins[j] = np.floor( num / 2**(7-j) )
                num = num - spins[j]*2**(7-j)
                if spins[j]==0 : spins[j] = -1
            bweight = np.exp( -hamiltonian( spins, H ) / T )
            binn = int( magnetisation(spins)  + 8 ) 
            counts[binn] = counts[binn] + bweight
            Z = Z + bweight
  
        for i in range(17) : counts[i] = counts[i] / Z
        fighand=plt.gca()
        for k in range(17) :
           patch = fighand.patches[k]
           self.assertTrue( np.abs( patch.get_xy()[0] + 0.5*patch.get_width() - (-8+k) )<1e-7, "The marginal distribution you have computed is incorrect" )
           self.assertTrue( np.abs(patch.get_height() - counts[k] )<1e-7, "The marginal distribution you have computed is incorrect" )
