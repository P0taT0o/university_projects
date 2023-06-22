# lista 5

import numpy as np
import timeit
import scipy.stats as stats
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# zadanie 1

# Box-Muller

def box_muller():
    E = np.random.exponential()
    Theta = np.random.uniform(0, 2*np.pi)
    return np.sqrt(2*E)*np.cos(Theta), np.sqrt(2*E)*np.sin(Theta)

Z = [box_muller() for i in range(10**4)]
X = [Z[i][0] for i in range(10**4)]
Y = [Z[i][1] for i in range(10**4)]
plt.hist2d(X, Y, bins=100);
plt.show()

anderson_result = stats.anderson(X, dist='norm')
jb_result = stats.jarque_bera(X)

print(f"Anderson-Darling test result for Box-Muller: {anderson_result}")
print(f"Jarque-Bera test result for Box-Muller: {jb_result}")

# Marsaglia

def marsaglia():
    X,Y = np.random.uniform(-1, 1, 2)
    while X**2 + Y**2 > 1:
        X,Y = np.random.uniform(-1, 1, 2)
    R = X**2 + Y**2
    return X/np.sqrt(R) * np.sqrt(-2*np.log(R)), Y/np.sqrt(R) * np.sqrt(-2*np.log(R))

Z = [marsaglia() for i in range(10**4)]
X = [Z[i][0] for i in range(10**4)]
Y = [Z[i][1] for i in range(10**4)]
plt.hist2d(X, Y, bins=100);
plt.show()

anderson_result = stats.anderson(X, dist='norm')
jb_result = stats.jarque_bera(X)

print(f"Anderson-Darling test result for Marsaglia: {anderson_result}")
print(f"Jarque-Bera test result for Marsaglia: {jb_result}")

# times

elapsed_time_box_muller = timeit.timeit(box_muller, number=100000)
elapsed_time_marsaglia = timeit.timeit(marsaglia, number=100000)

print(f"Box-Muller time: {elapsed_time_box_muller}")
print(f"Marsaglia time: {elapsed_time_marsaglia}")

# zadanie 2

# matrix 2x2

mu = np.zeros(2)
Sigma = np.array([[2, 1], [1, 3]])

W = np.random.multivariate_normal(mu, Sigma, 10000)
X = W[:, 0]
Y = W[:, 1]

anderson_result = stats.anderson(X, dist='norm')
print(f"Anderson-Darling test result for matrix 2x2: {anderson_result}")
corr_result = stats.pearsonr(X, Y)
print(f"Pearson correlation test result for matrix 2x2: {corr_result}")

plt.scatter(x=X, y=Y, alpha=0.5, s=4)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# 1. matrix 3x3

mu = np.zeros(3)
Sigma = np.array([[2, -0.5, 1], [-0.5, 2.25, 0], [1, 0, 2]])

W = np.random.multivariate_normal(mu, Sigma, 10000)
X = W[:, 0]
Y = W[:, 1]
Z = W[:, 2]

anderson_result = stats.anderson(X, dist='norm')
print(f"Anderson-Darling test result for first matrix 3x3: {anderson_result}")
corr_result = stats.pearsonr(X, Y)
print(f"Pearson correlation test result for first matrix 3x3: {corr_result}")

fig = plt.figure()
ax = plt.axes(projection ="3d")
ax.scatter3D(xs=X, ys=Y, zs=Z, alpha=0.5, s=4)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# 2. matrix 3x3

mu = np.zeros(3)
Sigma = np.array([[3.0, -0.5, -0.5], [0.5, 2.25, 1.5], [-0.5, 1.5, 1.25]])

W = np.random.multivariate_normal(mu, Sigma, 10000)
X = W[:, 0]
Y = W[:, 1]
Z = W[:, 2]

anderson_result = stats.anderson(X, dist='norm')
print(f"Anderson-Darling test result for second matrix 3x3: {anderson_result}")
corr_result = stats.pearsonr(X, Y)
print(f"Pearson correlation test result for second matrix 3x3: {corr_result}")

fig = plt.figure()
ax = plt.axes(projection ="3d")
ax.scatter3D(xs=X, ys=Y, zs=Z, alpha=0.5, s=4)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()