# lista 6 

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def poisson_process(T, lamb):
    interarrival_times = np.random.exponential(scale=1/lamb, size=int(np.ceil(lamb*T)))
    jump_times = np.cumsum(interarrival_times)
    jump_times = jump_times[jump_times < T]
    return jump_times

jump_times = poisson_process(10, 1.5)
print("Czas skoków:", jump_times)

plt.plot(jump_times, np.arange(len(jump_times)),drawstyle='steps-post')
plt.xlabel("czas")
plt.show()

jump_times = poisson_process(10000, 1.5)
print("Czas skoków:", jump_times)
plt.plot(jump_times, np.arange(len(jump_times)),drawstyle='steps-post')
plt.xlabel("czas")
plt.show()

def compute_N(t, times):
    # znalezienie indeksu pierwszej wartości większej lub równej t
    Nt = np.searchsorted(times, t)
    return Nt

t = 5
Ns = [compute_N(t, poisson_process(10, 2)) for _ in  range(10000)]
plt.hist(Ns, bins=20)
plt.show()

sns.ecdfplot(Ns)

x = np.arange(0, 45, 0.001)
dist = lambda x: stats.poisson.cdf(x, 2*t)
y = dist(x)
plt.plot(x, y)
plt.show()

samples_poisson_theoretical=np.random.poisson(2*t,size=10**4)
print(stats.kstest(Ns,samples_poisson_theoretical))