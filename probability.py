"""
Module to contain a few util functions related to Probability
"""

def Factorial(n):
    """
    Method to find factorial of a given number
    """
    if n == 1 or n==0:
        return 1
    else:
        return n * Factorial(n-1)

def Combination(n, r):
    """
    Function to find the combination.
    n = Total number of items
    r = represents the number of items being chosen at a time
    """
    y = Factorial(n)/(Factorial(r)* Factorial(n-r))
    return y

def BinominalDistribution(n):
    """
    Function to calculate a binomial distibution for 2 outcome problems
    eg: coin toss

    n: No of times the event is happening
    """
    l = []
    for i in range(n+1):
        p = Combination(n,i)/(2**n)
        l.append(p)
    return l

def main():
    plt.plot( [i for i in range(16)], BinominalDistribution(16))
    plt.show()
    
if __name__="__main__":
  main()
