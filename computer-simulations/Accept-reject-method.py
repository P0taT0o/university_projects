# lista 3

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# zadanie 1

def g(x, alpha):
    return (alpha+1) * x**alpha

def rejection_sampling(num_samples, alpha):
    samples = []
    num_rejected = 0
    c = (alpha+1) / (1**(alpha+1))  # wartość stałej C_alpha
    while len(samples) < num_samples:
        x = np.random.uniform(0,1)
        u = np.random.uniform(0, c)
        if u <= g(x,alpha):
            samples.append(x)
        else:
            num_rejected += 1
    acceptance_rate = len(samples) / num_samples
    print("Alpha = {}, Acceptance rate: {:.5f}".format(alpha, acceptance_rate))
    print("Number of rejected samples:", num_rejected)
    return samples

alpha = 2
samples = rejection_sampling(10000, alpha)
plt.hist(samples, bins=50, density=True)
c = alpha+1
x = np.linspace(0, 1, 1000)
y = c * x**alpha
plt.plot(x, y, 'r')
plt.title("zadanie 1 dla alpha=2")
plt.show()

# zadanie 2

def g2(x):
    return  2/(math.pi)*np.sin(x)

def rejection_sampling2(num_samples):
    samples = []
    num_rejected = 0
    while len(samples)<num_samples:
        x=np.random.uniform(0,math.pi/2)
        u=np.random.uniform(0,1)
        if u<=g2(x):
            samples.append(x)
        else:
            num_rejected+=1
    acceptance_rate = len(samples) / num_samples
    print("Acceptance rate:", acceptance_rate)
    print("Number of rejected samples:", num_rejected)
    return samples

samples = rejection_sampling2(100000)
plt.hist(samples, bins=30, density=True)
x = np.linspace(0, math.pi/2, 1000)
y = np.sin(x)
plt.plot(x, y, 'r')
plt.title("zadanie 2")
plt.show()

# Y=X^2

def g3(x):
    return (math.pi**2/7)*np.sin(x**(0.5))/ (2*x**(0.5))

def rejection_sampling3(num_samples, max_rejects=100000):
    samples = np.zeros(num_samples)
    num_generated = 0
    num_accepted = 0
    num_rejected = 0
    while num_accepted < num_samples and num_rejected < max_rejects:
        x = np.random.uniform(0, np.pi/2)
        u = np.random.uniform(0, 1)
        if u <= g3(x):
            samples[num_accepted] = x
            num_accepted += 1
        else:
            num_rejected += 1
        num_generated += 1
        acceptance_rate = len(samples) / num_samples
    print("Acceptance rate:", acceptance_rate)
    print("Number of rejected samples:", num_rejected)
    return samples[:num_accepted]

samples = rejection_sampling3(100000)
plt.hist(samples, bins=100, density=True, range=(0, np.pi/2))
x = np.linspace(0.001, np.pi/2, 1000)
y = g3(x)
plt.plot(x, y, 'r')
plt.title("zadanie 2 dla Y=X^2")
plt.show()

# uzyskanie X jako sqrt(Y)

samples = np.sqrt(rejection_sampling3(100000))
plt.hist(samples, bins=30, density=True)
x = np.linspace(0, 1.3, 1000)
y = ((math.pi**2)/7)*np.sin(x)
plt.plot(x, y, 'r')
plt.title("zadanie 2 dla X uzyskanego jako sqrt(Y)")
plt.show()

# zadanie 3

def generate_halfnormal_from_exponential(n, lambda_=1):
    half_norm = np.zeros(n)
    i = 0
    while i < n:
        exp_rand = random.expovariate(1/lambda_)
        u = np.random.rand()
        if u <= np.exp(-(exp_rand**2)/2 - 1/2 * lambda_**2 + lambda_*exp_rand):
            half_norm[i] = exp_rand
            i += 1
    return half_norm

n = 10000
generate_halfnormal_from_exponential(n)
plt.hist(generate_halfnormal_from_exponential(n), bins=50, density=True)
x = np.linspace(0,4,10000)
plt.plot(x, stats.halfnorm.pdf(x),'r')
plt.title("zadanie 3 - rozkład połnormalny")
plt.show()

# generowanie rozkladu normlanego z wczesniej wygenerowanego polnormlanego

samples = generate_halfnormal_from_exponential(100000)
xs = [random.choice([-1,1])*sample for sample in samples]
plt.hist(xs, density=True, bins=70)
x = np.linspace(-4,4,10000)
plt.plot(x, stats.norm.pdf(x,scale=1),'r')
plt.title("zadanie 3 - rozkład normalny")
plt.show()
