# lista 4

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# rozklad cauchy'ego

def generate_cauchy(n):
    samples = []
    while len(samples)<n:
        x, y = np.random.uniform(0, 1), np.random.uniform(-1, 1)
        if x**2+y**2<=1:
            samples.append(y/x)
    return samples

samples = generate_cauchy(10000)
plt.hist(samples, bins=np.arange(-20,20,0.5), density=True)
x = np.arange(-20,20,0.001)
plt.plot(x,stats.cauchy.pdf(x,0,1), c="r")
plt.title("rozkład Cauchy'ego")
plt.show()

# rozklad normlany

def generate_normal(n):
    samples = []
    while len(samples)<n:
        x, y = np.random.uniform(0, 1), np.random.uniform(-2/np.e, 2/np.e)
        if x**2<= np.exp(-(y/x)**2):
            samples.append(y/x)
    return samples

samples = generate_normal(10000)
plt.hist(samples, bins=100, density=True)
x = np.arange(-4,4,0.001)
plt.plot(x,stats.norm.pdf(x, scale=0.5**0.5), c="r")
plt.title("rozkład normlany")
plt.show()