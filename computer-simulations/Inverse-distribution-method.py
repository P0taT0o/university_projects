# lista 2 - SYmulacje Komputerowe

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
from scipy.special import erfinv
import timeit
import math
from statsmodels.distributions.empirical_distribution import ECDF

# zadanie 1

# rozkład wykladniczy

def inverse_exp(lam, n):
    u = np.random.uniform(0,1,size=n)
    return -np.log(u)/lam

samples_exp = inverse_exp(1, 10000)

# gęstość
plt.hist(samples_exp, bins=50, density=True)
x = np.arange(0,10,0.001)
plt.plot(x,expon.pdf(x,loc=0), c="r")
plt.title("Gęstość rozkładu wykładniczego")
plt.show()

starttime=timeit.default_timer()
inverse_exp(1,10000)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
expon.pdf(x)
endtime=timeit.default_timer()
print(endtime-starttime)

# dystrybuanta
x = np.linspace(0,10,10000)
F = expon.cdf(x, 0)
plt.plot(x,F)
ecdf = ECDF(samples_exp)
plt.plot(ecdf.x, ecdf.y)
plt.title("Dystrybuanta rozkładu wykładniczego")
plt.show()

starttime=timeit.default_timer()
ecdf = ECDF(samples_exp)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
expon.cdf(x, 0)
endtime=timeit.default_timer()
print(endtime-starttime)

#rozklad normalny

def normal_inv_cdf(mu, sigma, size):
    u = np.random.uniform(size=size)
    return mu + sigma*np.sqrt(2)*erfinv(2*u-1)

samples_normal = normal_inv_cdf(1, 2, 1000)

# gęstość
plt.hist(samples_normal, bins=50, density=True)
x = np.arange(-10,10,0.001)
plt.plot(x,norm.pdf(x,1,2), c="r")
plt.title("Gęstość rozkładu normlanego")
plt.show()

starttime=timeit.default_timer()
normal_inv_cdf(1,2,10000)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
norm.pdf(x,1,2)
endtime=timeit.default_timer()
print(endtime-starttime)

# dystrybuanta
x = np.linspace(-10,10,10000)
plt.plot(x,norm.cdf(x,1,2), c='r')
ecdf = ECDF(samples_normal)
plt.plot(ecdf.x, ecdf.y)
plt.title("Dystrybuanta rozkładu normlanego")
plt.show()

starttime=timeit.default_timer()
ecdf = ECDF(samples_normal)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
norm.cdf(x,1,2)
endtime=timeit.default_timer()
print(endtime-starttime)

# rozklad Cauchy'ego

def cauchy_inv_cdf(mu, gamma, size):
    u = np.random.uniform(size=size)
    return mu + gamma*np.tan(np.pi*(u-0.5))

samples_cauchy = cauchy_inv_cdf(0, 1, 10000)

# gestosc
plt.hist(samples_cauchy, bins=range(-20,20,1), density=True)
x = np.arange(-20,20,0.001)
plt.plot(x,cauchy.pdf(x,0,1), c="r")
plt.title("Gęstość rozkładu Cauchy'ego")
plt.show()

starttime=timeit.default_timer()
cauchy_inv_cdf(0,1,10000)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
cauchy.pdf(x,0,1)
endtime=timeit.default_timer()
print(endtime-starttime)

# dystrybuanta
x = np.linspace(-5,5,1000)
plt.plot(x,cauchy.cdf(x), c='r')
ecdf = ECDF(samples_cauchy)
plt.plot(ecdf.x, ecdf.y)
plt.xlim(-5,5)
plt.title("Dystrybuanta rozkładu Cauchy'ego")
plt.show()

starttime=timeit.default_timer()
ECDF(samples_cauchy)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
cauchy.cdf(x)
endtime=timeit.default_timer

# zadanie 2

# rozklad geometryczny

def geom_inv_cdf(p, size):
    u = np.random.uniform(size=size)
    return np.floor(np.log(u)/np.log(1-p))

samples_geom = geom_inv_cdf(0.5, 10000)

# dystrybuanta
ecdf = ECDF(samples_geom)
plt.step(ecdf.x, ecdf.y)
x = np.linspace(0,10,1000)
F = geom.cdf(x, 0.5, loc = -1)
plt.step(x,F, 'r')
plt.title("Dystrybuanta rozkładu geometrycznego")
plt.show()

starttime=timeit.default_timer()
ECDF(samples_geom)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
geom.cdf(x, 0.5, loc = -1)
endtime=timeit.default_timer

# rozklad Poissona

def poisson_inv_cdf(lamb, size):
    x = np.zeros(size, dtype=np.int64)
    for i in range(size):
        u = np.random.uniform(0,1)
        k = 0
        F = math.exp(-lamb)
        while u - F > 0:
            k += 1
            F += (math.exp(-lamb) * lamb**k) / math.factorial(k)
        x[i] = k
    return x

samples_poiss = poisson_inv_cdf(10, 10000)

# dystrybuanta
ecdf = ECDF(samples_poiss)
plt.step(ecdf.x, ecdf.y)
x = np.linspace(0,20,10000)
plt.step(x, poisson.cdf(x,10), 'r')
plt.title("Dystrybuanta rozkładu Poissona")
plt.show()

starttime=timeit.default_timer()
ECDF(samples_poiss)
endtime=timeit.default_timer()
print(endtime-starttime)

starttime=timeit.default_timer()
poisson.cdf(x,10)
endtime=timeit.default_timer

# zadanie 3

def array_inverse(p):
    q = np.sum(p)
    array = np.zeros(q)
    for i in range(len(p)):
        array[sum(p[:i]):sum(p[:i+1])] = i+1
    return array

def random_i_array(p, n):
    I = np.floor(np.random.random(n)*sum(p))
    I = I.astype('int32')
    array = array_inverse(p)
    return np.array([array[i] for i in I])

def count_values(x, array):
    val = np.array([np.count_nonzero(array == i) for i in x])/len(array)
    return val

def distribution(p, n):
    q = sum(p)
    pk = np.array(p) /q
    x = [i+1 for i in range(len(p))]
    result = random_i_array(p, n)
    count1 = count_values(x, result)
    dist_dict = {}
    for i in range(len(pk)):
        dist_dict[pk[i]] = count1[i]
    return dist_dict