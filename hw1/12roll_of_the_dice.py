from random import randint

import scipy as scipy
from matplotlib import ticker
from numpy import asarray
import matplotlib.pyplot as plt
import numpy as np

frequency = []
array = []
for i in range(1, 1001):
    throw1 = randint(1, 6)
    throw2 = randint(1, 6)
    array.append(throw1+throw2 )
print(array)
for i in range (2,13):
    frequency.append(array.count(i))
for i in range (2,13):
    print(f'frequency of occurrence of a digit {i} is {frequency[i-2]} ')


fig, ax = plt.subplots(1,1)
ax.plot(frequency)
plt.show()