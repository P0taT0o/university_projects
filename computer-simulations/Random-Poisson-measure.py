# LISTA 9

import random
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
import math

######################################
# ZADANIE 1
######################################

# Generowanie losowej miary Poissonowskiej dla zbioru liczb {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
def generate_poisson_measure_set1(lmbda):
    omega = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    poisson_count = np.random.poisson(lmbda * len(omega))
    points = random.choices(omega, k=poisson_count)
    return points

lambda_val = 1
measure_set1 = generate_poisson_measure_set1(lambda_val)
print("Poisson Measure Set for numbers {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:")
print(measure_set1)

# wizualizacja
plt.hist(measure_set1, bins=np.arange(0.5, 10.5))
plt.title("Poisson Measure Set for numbers {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}")
plt.show()

# Generowanie losowej miary Poissonowskiej dla sześcianu
def generate_poisson_measure_cube(lmbda, side_length):
    volume = side_length ** 3
    poisson_count = np.random.poisson(lmbda * volume)
    points = []
    for _ in range(poisson_count):
        x = random.uniform(0, side_length)
        y = random.uniform(0, side_length)
        z = random.uniform(0, side_length)
        points.append((x, y, z))
    return points

lambda_val = 10
side_length_val = 5
measure_cube = generate_poisson_measure_cube(lambda_val, side_length_val)
print("Poisson Measure Set for a cube:")
print(measure_cube)

measure_cube_x = [point[0] for point in measure_cube]
measure_cube_y = [point[1] for point in measure_cube]
measure_cube_z = [point[2] for point in measure_cube]
ax = plt.subplot(projection='3d')
ax.scatter(measure_cube_x, measure_cube_y, measure_cube_z)
ax.set_title("Poisson Measure Set for a cube")
plt.show()

# Generowanie losowej miary Poissonowskiej dla koła
def generate_poisson_measure_circle(lmbda, radius):
    area = math.pi * radius ** 2
    poisson_count = np.random.poisson(lmbda * area)
    points = []
    while len(points) < poisson_count:
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        if x**2 + y**2 <= radius**2:
            points.append((x, y))
    return points

radius_val = 2
lambda_val = 100
measure_circle = generate_poisson_measure_circle(lambda_val, radius_val)
print("Poisson Measure Set for a circle:")
print(measure_circle)

# wizualizacja
measure_circle_x = [point[0] for point in measure_circle]
measure_circle_y = [point[1] for point in measure_circle]
plt.scatter(measure_circle_x, measure_circle_y)
plt.title("Poisson Measure Set for a circle")
plt.axis('equal')
plt.show()

######################################
# ZADANIE 2
######################################

# Funkcja generująca niejednorodną losową miarę Poissonowską na kole
def generate_nonhomogeneous_poisson_measure_circle(lmbda, radius, max_intensity):
    points = []
    max_count = int(math.ceil(max_intensity * math.pi * radius**2))
    for _ in range(max_count):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        point = (x, y)
        if x**2 + y**2 <= radius**2:
            points.append(point)
    points2 = []
    for point in points:
        intensity = math.exp(-point[0]**2- point[1]**2)
        if random.uniform(0, 1) <= intensity :
            points2.append(point) 
    return points2

# Parametry
lambda_val = 100000
radius_val = 2
max_intensity_val = lambda_val * math.exp(-radius_val**2)

# Wygenerowanie niejednorodowej losowej miary Poissonowskiej na kole
measure_circle = generate_nonhomogeneous_poisson_measure_circle(lambda_val, radius_val, max_intensity_val)
print("Nonhomogeneous Poisson Measure Set for a circle:")
print(measure_circle)

# Wizualizacja wyników
measure_circle_x = [point[0] for point in measure_circle]
measure_circle_y = [point[1] for point in measure_circle]
plt.scatter(measure_circle_x, measure_circle_y, s=10)
plt.title("Nonhomogeneous Poisson Measure Set for a circle")
plt.axis('equal')
plt.show()

######################################
# ZADANIE 3
######################################

# Funkcja generująca miarę na kole jednostkowym o losowej intensywności
def generate_random_intensity_measure_circle(lmbda, r):
    x0, y0 = np.random.uniform(-1+r, 1-r), np.random.uniform(-1+r, 1-r)
    while x0**2 + y0**2 > (1-r)**2:
        x0, y0 = np.random.uniform(-1+r, 1-r), np.random.uniform(-1+r, 1-r)
    
    N = np.random.poisson(lmbda * math.pi * r**2)
    points = []
    i = 0
    while i < N:
        x, y = np.random.uniform(-r, r), np.random.uniform(-r, r)
        if (x+x0)**2 + (y+y0)**2 <= 1 and x**2 + y**2 <= r**2:
            points.append([x+x0, y+y0])
            i += 1
    
    return np.array(points).T

lmbda_val = 5000
r_val = 0.1

fig, axes = plt.subplots()

for _ in range(13):
    measure_circle = generate_random_intensity_measure_circle(lmbda_val, r_val)
    axes.scatter(measure_circle[0], measure_circle[1], s=1)

c = plt.Circle((0,0), 1, fill = False, color = 'black')
axes.add_patch(c)
axes.set_xlim((-1.2,1.2))
axes.set_ylim((-1.2,1.2))
axes.set_aspect('equal')
plt.title("Random Intensity Measure Set on a Unit Circle")
plt.xlabel("x")
plt.ylabel("y")
plt.show()