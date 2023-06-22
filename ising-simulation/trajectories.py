import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from time import perf_counter

@njit(fastmath=True)
def simulate(spins, temperature, num_steps):
    N = len(spins)       
    magnetizations = np.zeros(num_steps)
    for step in range(num_steps):
        for _ in range(N*N):
            L = spins.shape[0]
            i, j = np.random.randint(0, L, size=2)
            spin = spins[i, j]
            i2, j2 = i+1, j+1
            neighbors_sum = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
            energy_diff = 2 * spin * neighbors_sum
            if energy_diff <= 0 or np.random.rand() < np.exp(-energy_diff / temperature):
                spins[i, j] *= -1
        magnetizations[step]=np.sum(spins) / (N * N)
    return magnetizations

def plot_trajectories(L, num_steps, temperature):
    num_trajectories=10
    trajectories = []
    for t in range(num_trajectories):
        spins = np.random.choice([-1, 1], size=(L, L))
        magnetization = (simulate(spins, temperature,num_steps))
        trajectories.append(magnetization)
        
    plt.figure(figsize=(10,7))
    for i, trajectory in enumerate(trajectories):
        plt.plot(range(len(trajectory)), trajectory)
    plt.title(f"Trajektoria dla L={L}, T={temperature}")
    plt.xlabel("t [MCS]")
    plt.ylabel("m")
    plt.ylim((-1,1))
    plt.xlim((0,num_steps))
    plt.savefig(f"trajektoria_L{L}_T{temperature}.jpg")

#plot_trajectories(L = 10, temperature = 1, num_steps = 150)
#plot_trajectories(L = 20, temperature = 1, num_steps = 500)
#plot_trajectories(L = 40, temperature = 1, num_steps = 1000)
#plot_trajectories(L = 80, temperature = 1, num_steps = 2000)

T = 0.5
plot_trajectories(L = 10, temperature = T, num_steps = 800)
plot_trajectories(L = 20, temperature = T, num_steps = 800)
plot_trajectories(L = 40, temperature = T, num_steps = 1500)
plot_trajectories(L = 80, temperature = T, num_steps = 3000)

T = 2.27
#plot_trajectories(L = 10, temperature = T, num_steps = 500)
#plot_trajectories(L = 20, temperature = T, num_steps = 1000)
plot_trajectories(L = 40, temperature = T, num_steps = 2000)
plot_trajectories(L = 80, temperature = T, num_steps = 5000)

T = 10
#plot_trajectories(L = 10, temperature = T, num_steps = 500)
#plot_trajectories(L = 20, temperature = T, num_steps = 500)
#plot_trajectories(L = 40, temperature = T, num_steps = 1000)
plot_trajectories(L = 80, temperature = T, num_steps = 1000)