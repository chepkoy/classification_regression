# Simple lineplot

import matplotlib.pyplot as plt
import numpy as np

list_one = np.linspace(0, 10, 100)
list_two = np.exp(-list_one)

plt.plot(list_one, list_two)

plt.show()

# Ploting a histogram

from numpy.random import normal, rand

x = normal(size= 200)
plt.hist(x, bins=30)
plt.show()