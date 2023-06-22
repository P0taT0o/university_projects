# lista 7

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
from scipy.integrate import quad
sns.set()

# ZADANIE 1

def lamb(t):
    return np.sin(t) + 2

def cumulative_intensity(t):
    result, _ = quad(lamb, 0, t)
    return result

def nonhomogeneous_poisson_process(T, lamb):
    t = 0
    ts = []
    λmax = np.max(lamb(np.arange(0, T, 0.01)))

    while t < T:
        t += np.random.exponential(scale=λmax**(-1))

        if np.random.rand() < lamb(t) / λmax:
            if t < T:
                ts.append(t)

    return ts

T = 10
ts = nonhomogeneous_poisson_process(T, lamb)

plt.scatter([0], [0], color='black', label='_nolegend_')
plt.scatter(ts, np.arange(len(ts))-1, edgecolor='black', facecolor='none')
plt.scatter(ts, np.arange(1, len(ts)+1)-1, color='black')
for i in range(len(ts) - 1):
    plt.plot([ts[i], ts[i+1]], [i, i], color='black')

plt.plot([0, ts[0]], [0, 0], color='black')
plt.plot([ts[-1], T], [len(ts)-1, len(ts)-1], color='black')

t_values = np.arange(0, T+0.1, 0.1)
l_values = [cumulative_intensity(t) for t in t_values]
plt.plot(t_values, l_values, linewidth=2)
plt.xlabel('t')
plt.ylabel('ilość zdarzeń')
plt.title("Metoda przerzedzenia dla T=10")
plt.show()

def cumulative_intensity(t):
    result, _ = quad(lamb, 0, t)
    return result

def Ns(t, ts):
    return np.sum(np.array(ts) <= t)

ns = np.empty(1000)
t = 5

for i in range(1000):
    ns[i] = Ns(t, nonhomogeneous_poisson_process(T, lamb))

plt.figure()
plt.hist(ns, density=True, bins=np.arange(-0.5, 26.5, 1))
plt.plot(np.arange(0, 26), [stats.poisson.pmf(x, cumulative_intensity(t)) for x in np.arange(0, 26)])
plt.title("Porównanie funkcji rozkładu dla metody przerzedzenia")
plt.show()

# ZADANIE 2

def lamb(t):
    return t

def nonhomogeneous_poisson_process2(T):
    Ns = np.random.poisson(cumulative_intensity(T))
    ts = np.sqrt(np.random.rand(Ns) * 2 * cumulative_intensity(T))
    ts.sort()
    return ts

T = 10
ts = nonhomogeneous_poisson_process2(T)

plt.scatter([0], [0], color='black')
plt.scatter(ts, np.arange(len(ts)), edgecolor='black', facecolor='none')
plt.scatter(ts, np.arange(1, len(ts)+1), color='black')

for i in range(len(ts)-1):
    plt.plot([ts[i], ts[i+1]], [i+1, i+1], color='black')
    
plt.plot([0, ts[0]], [0, 0], color='black')
plt.plot([ts[-1], T], [len(ts)-1, len(ts)-1], color='black')

t_values = np.arange(0, T+0.1, 0.1)
l_values = [cumulative_intensity(t) for t in t_values]
plt.plot(t_values, l_values, linewidth=2)

plt.xlabel('t')
plt.ylabel('ilość zdarzeń')
plt.title('Metoda odwrotnej dystrybuanty')
plt.show()

def Ns(t, ts):
    return np.sum(np.array(ts) <= t)

ns = np.empty(1000)
t = 5

for i in range(1000):
    ns[i] = Ns(t, nonhomogeneous_poisson_process2(T))

plt.figure()
plt.hist(ns, density=True, bins=np.arange(-0.5, 26.5, 1))
plt.plot(np.arange(0, 26), [stats.poisson.pmf(x, cumulative_intensity(t)) for x in np.arange(0, 26)])
plt.title("Porównanie funkcji rozkładu dla metody odwrotnej dystrybuanty")
plt.show()

# ZADANIE 3

def combine(T, lamb1, lamb2):
    t1 = nonhomogeneous_poisson_process(T, lamb1)
    t2 = nonhomogeneous_poisson_process(T, lamb2)
    ts = np.concatenate((t1, t2))
    ts.sort()
    return ts

T = 100

def lamb1(t):
    return np.sin(t) + 1

def lamb2(t):
    return np.cos(t) + 1

ts = combine(T, lamb1, lamb2)

plt.scatter([0], [0], color='black')
plt.scatter(ts, np.arange(len(ts)), edgecolor='black', facecolor='none')
plt.scatter(ts, np.arange(1, len(ts)+1), color='black')

for i in range(len(ts)-1):
    plt.plot([ts[i], ts[i+1]], [i+1, i+1], color='black')
    
plt.plot([0, ts[0]], [0, 0], color='black')
plt.plot([ts[-1], T], [len(ts)-1, len(ts)-1], color='black')

def cumulative_intensity_combined(t):
    result1, _ = quad(lamb1, 0, t)
    result2, _ = quad(lamb2, 0, t)
    return result1 + result2

t_values = np.arange(0, T+0.1, 0.1)
l_values = [cumulative_intensity_combined(t) for t in t_values]
plt.plot(t_values, l_values, linewidth=2)

plt.xlabel('t')
plt.ylabel('ilość zdarzeń')
plt.title('Łączone procesy Poissona')
plt.show()

# ZADANIE 4

def MarkedPoissonProcess(T, apk):
    ts = nonhomogeneous_poisson_process2(T)
    marks = np.random.choice(a=3, size=len(ts), p=apk / np.sum(apk))
    ts_1 = ts[marks == 0]
    ts_2 = ts[marks == 1]
    ts_3 = ts[marks == 2]
    return ts, ts_1, ts_2, ts_3

T = 10
apk = np.array([1, 1, 1])

ts, t1, t2, t3 = MarkedPoissonProcess(T, apk)

# 1 wykres
plt.scatter([0], [0], marker='o', color='black', label=None)
plt.scatter(ts, np.arange(len(ts))-1, marker='o', edgecolor='black', facecolor='none', label=None)
plt.scatter(ts, np.arange(1, len(ts)+1)-1, marker='o', color='black', label=None)

for i in range(len(ts)-1):
    plt.plot([ts[i], ts[i+1]], [i, i], color='black')

plt.plot([0, ts[0]], [0, 0], color='black')
plt.plot([ts[-1], T], [len(ts)-1, len(ts)-1], color='black')

# 2 wykres

plt.scatter([0], [0], marker='D', color='orange', label=None)
plt.scatter(t1, np.arange(len(t1))-1, marker='D', edgecolor='orange', facecolor='none', label=None)
plt.scatter(t1, np.arange(1, len(t1)+1)-1, marker='D', color='orange', label=None)

for i in range(len(t1)-1):
    plt.plot([t1[i], t1[i+1]], [i, i], color='orange')

plt.plot([0, t1[0]], [0, 0], color='orange')
plt.plot([t1[-1], T], [len(t1)-1, len(t1)-1], color='orange')

# 3 wykres

plt.scatter([0], [0], marker='H', color='blue', label=None)
plt.scatter(t2, np.arange(len(t2))-1, marker='H', edgecolor='blue', facecolor='none', label=None)
plt.scatter(t2, np.arange(1, len(t2)+1)-1, marker='H', color='blue', label=None)

for i in range(len(t2)-1):
    plt.plot([t2[i], t2[i+1]], [i, i], color='blue')

plt.plot([0, t2[0]], [0, 0], color='blue')
plt.plot([t2[-1], T], [len(t2)-1, len(t2)-1], color='blue')

# 4 wykres

plt.scatter([0], [0], marker='*', color='green', label=None)
plt.scatter(t3, np.arange(len(t3))-1, marker='*', edgecolor='green', facecolor='none', label=None)
plt.scatter(t3, np.arange(1, len(t3)+1)-1, marker='*', color='green', label=None)

for i in range(len(t3)-1):
    plt.plot([t3[i], t3[i+1]], [i, i], color='green')

plt.plot([0, t3[0]], [0, 0], color='green')
plt.plot([t3[-1], T], [len(t3)-1, len(t3)-1], color='green')

plt.xlabel('t')
plt.ylabel('ilosc zdarzen')
plt.title('Rozłączenie procesów')
plt.show()