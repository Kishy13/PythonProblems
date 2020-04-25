import numpy as np
import pandas as pd

x = np.reshape(range(20),(5,4))
l = []
for item in np.nditer(x):
    if item%2 == 0:
        l.append(item)
    else:
        l.append(0)
y = np.array(l).reshape(5,4)
print(y)
    
