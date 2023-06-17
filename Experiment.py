# Experiment Class
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

class Experiment:
    """Start experiment by describing the data to be used:\n
            x = number of successes in the experiment\
            y = number of failures in the experiment\
            exp_number = experiment name/number"""

    def __init__(self,x,y,exp_number):

        self.exp_number = exp_number
        self.n = x + y
        self.p = x/self.n
        self.q = 1 - self.p
        self.games = list(range(self.n + 1))
        
    def mean(self,m=False):
        """Returns the mean using the binom library.\
            m=True to calculate manually."""
        if m==True:
            mean = self.n*self.p
        else:
            mean = binom.stats(self.n, self.p)[0]
        return (mean)
    
    def variance(self,m=False):
        """Returns the variance using the binom library.\
            m=True to calculate manually."""
        from scipy.stats import binom
        if m==True:
            var = self.n * self.p * self.q
        else:
            var = binom.stats(self.n, self.p)[1]
        return (var)
    
    def mass_function(self):
        """Returns the probability mass function."""
        from scipy.stats import binom
        dist = [binom.pmf(g, self.n, self.p) for g in self.games]
        return (dist)
    
    def conf_int(self,confidence,m=[False,1.96]):
        """Returns a list with the lower and upper limites of the confidence interval, respectively.\
        confidence = confidence level (between 0 and 1) \
        m=[True,zValue] to calculate manually. Only returns proportionally in this case."""
        if m[0]==True:
            # Considers 95% confidence by default    
            z = m[1]
            constant_term = z*np.sqrt(self.p*self.q/self.n)
            pos_term = round(self.p + constant_term,5)
            neg_term = round(self.p - constant_term,5)
            inter = [neg_term,pos_term]
            return inter
        else:   
            from scipy.stats import binom
            xtremes = binom.interval(confidence, self.n, self.p, loc=0)
            inter = [round(value/self.n,5) for value in xtremes]
            return (xtremes,inter)
        
    def plot_mass_function(self,zoomed=[False,[0,0]]):
        """Plots the mass function of the experiment.\
        zoomed=[True,[lowerLimit,HigherLimit]] to print a zoomed graph"""
        plt.scatter(self.games, self.mass_function(),s=2)
        plt.xlim([0,self.n]) 
        plt.minorticks_on()
        plt.tick_params('both',length=5)
        plt.grid()
        if zoomed[0]==True:
            plt.xlim([zoomed[1][0]-50,zoomed[1][1]+50])
            plt.title('Experiment {}\n Binomial mass function (zoomed)'.format(self.exp_number))
            plt.show()
            return           
        else:
            plt.title('Experiment {}\n Binomial mass function'.format(self.exp_number))            
            plt.show()
            return