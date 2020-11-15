# Marginal distributions

The distribution of magnetisation values that you have just computed is not consistent with the average magnetisation that you can compute for this quantity if you are at a low temperature and if there is a strong magnetic field.  Under such conditions the average magnetisation of the sample will be large.  The average for the distribution that you have calculated is, however, always equal to zero.  

The reason for this discrepancy is hopefully obvious - when we calculated the distribution of magnetisation values for the microstates in the previous exercise we did not use the values of the temperature or the magnetic field strength.   We should, therefore, not be surprised by the fact that temperature and magnetic field strength do not affect the distribution of magnetisation values for our microstates.  The question we should ask, however, is how do we incorporate these factors and thereby obtain a model that tells us the probability that the magnetisation takes a particular value for a particular value of the temperature and magnetic field strength?

We can answer this question by recognising that when the temperature and magnetic field are fixed the probabilities of being in all the microstates are not equal.  Instead, the probability of being in microstate ![](https://render.githubusercontent.com/render/math?math=x_i) is given by:

![](https://render.githubusercontent.com/render/math?math=P(\mathbf{x}_i)=\frac{e^{-\beta\H(\mathbf{x_i)}}{Z})

where ![](https://render.githubusercontent.com/render/math?math=\beta) is the inverse temperature, ![](https://render.githubusercontent.com/render/math?math=H(\mathbf{x}_i)) is the Hamiltonian and where ![](https://render.githubusercontent.com/render/math?math=Z) is the canonical partition function.  As such if the temperature and magnetic field are set to constant values the probability of having a particular value, ![](https://render.githubusercontent.com/render/math?math=M_i), for the magnetisation can be calculated as:

![](https://render.githubusercontent.com/render/math?math=P(M_i)=\frac{1}{Z}\sum_{j=1}^M\delta(M(\mathbf{x}_j)-M_i)e^{-\beta\H(\mathbf{x}_j)}\qquad\textrm{where}\delta(0)=1\quad\textrm{and}\delta(x)=0\qquad\textrm{if}\quad\x\ne\0)

In this expression the sum runs over all the microstates and ![](https://render.githubusercontent.com/render/math?math=M(\mathbf{x}_j)) is the magnetisation of microstate ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}_j).  

To complete the code in the box on the left you will need to complete the function called `magnetisation`, which calculates the magnetisation from the microscopic coordinates for the `spins`, and the function called `hamiltonian`, which computes the Hamiltonian for a 1D Ising model in a magnetic field, `H`:

As always ![](https://render.githubusercontent.com/render/math?math=s_{N%2B1}=s_1).

Once you have written the code to calculate the magnetisation and the Hamiltonian you will need to write code to generate every possible microstate a system of N=8 spins can adopt.  You will need to use your `magnetisation` function to evaluate the magnetisation for each of these microstates and your `hamiltonian` function to evaluate the energy of each microstate.  For each microstate you will then need to calculate the numerator in the expression for the probability above and add this to the appropriate element of the list called `probabilities` and to the variable called `Z`.  These two variables will eventually hold the unormalised probability of having each of the possible values for the magnetisation and the partition function respectively.   As you can see I have already written code that will calculate and plot the normalised probabilities for you.

Your calculations should be completed at a temperature T=1.5 and with a magnetic field H=0.2.



