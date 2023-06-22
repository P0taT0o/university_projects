import matplotlib.pyplot as plt
import builtins
import numpy as np
import random
import math

# zadanie 1 - Generatory LCG liczb pseudolosowych

def LCG(alpha, beta, x0, p, n):
    xs = [0] * n
    xs[0] = x0
    for i in range(1, n):
        xs[i] = (beta * xs[i-1] + alpha) % p
    return xs

xs = LCG(1, 7**5, 0, 2**31 - 1, 10**6)

plt.scatter(range(1, 10**6+1, 100), xs[::100], s=1)
plt.show()
plt.scatter(xs[:-1:100], xs[1::100], s=1)
plt.show()
plt.scatter([xs[i] for i in range(0,100000,50)], [xs[i+1] for i in range(0,100000,50)], s=1)
plt.show()

# zadanie 2 - Ciągi kwazilosowe, ciąg van der Corput

def van_der_corput(base, n):
    seq = []
    for i in range(1, n+1):
        vdc, denom = 0, 1
        while i > 0:
            denom *= base
            i, remainder = divmod(i, base)
            vdc += remainder / denom
        seq.append(vdc)
    return seq

xs = van_der_corput(3,10**6)

plt.scatter(range(1, 10**6+1, 100), xs[::100], s=1)
plt.show()
plt.scatter(xs[:-1:100], xs[1::100])
plt.show()

# zadanie 3 - Szacowanie liczby π

n = 100000

# liczby pseudolosowe z minimal standard LCG

xs = [x / (2**31 - 1) for x in LCG(1, 7**5, 0, 2**31 - 1, n)]
ys = [y / (2**31 - 1) for y in LCG(1, 6**5, 0, 2**31 - 1, n)]
estimated_pi = builtins.sum(1 for x, y in zip(xs, ys) if (x**2 + y**2)**0.5 <= 1)/ n * 4
print(f"LCG: {estimated_pi}")

# liczby kwazilosowe z ciągu Hamiltona

xs = van_der_corput(2,n)
ys = van_der_corput(3,n)
estimated_pi = builtins.sum(1 for x, y in zip(xs, ys) if (x**2 + y**2)**0.5 <= 1)/ n * 4
print(f"van der Corput: {estimated_pi}")

# liczby wybierane równomiernie z kwadratu

def calc_pi(n):
    xs = np.empty(n,dtype = float)
    ys = np.empty(n,dtype = float)
    sqrt_n = int(np.sqrt(n))
    for i in range(1, sqrt_n+1):
        for j in range(1, sqrt_n+1):
            xs[i + (j-1)*sqrt_n - 1] = 1/np.sqrt(n) * i
            ys[i + (j-1)*sqrt_n - 1] = 1/np.sqrt(n) * j
    counter = builtins.sum(1 for x, y in zip(xs, ys) if (x**2 + y**2)**0.5 <= 1)
    return counter/n * 4

print(f"rownomiernie: {calc_pi(n)}" )
# zadanie 4 - Igła Buffona

def buffon_needle(line_distance, needle_length, num_of_needles):
    count = 0
    for needle in range(num_of_needles):
        x = random.uniform(0, line_distance)
        angle = random.uniform(0,math.pi/2)
        if x <= (line_distance*math.sin(angle))/2:
            count += 1
    pi_estimate = (2 * needle_length * num_of_needles) / (line_distance * count)
    return pi_estimate

print(f"buffon: {buffon_needle(1,0.5,1000000)}")