import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def CoinSimulation(iNumber, fProbability, iSampleSize):
    """
    Function would provide you a array(vector) of number of heads in required sample set.
    Args:
    iNumber: No of coins tossed
    fProbability: Probability of the outcome expected (for coin toss it would be 0.5)
    iSampleSize: How many times does the trail repeat

    Retuns:
    nHeads: A vector(array) of No of heads

    """
    n = iNumber
    p = fProbability
    # Using a Binominal distribution since tossing a coin has only 2 outcomes.
    size = iSampleSize
    nHeads = np.random.binomial(n, p, size)
    return nHeads

def main():
    nHeads = CoinSimulation(16, 0.5, 100000)
    print(len(nHeads))
    plt.hist(nHeads, bins=range(18))
    plt.show()

if __name__ == "__main__":
    main()

