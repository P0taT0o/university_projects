import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from time import perf_counter

@njit(fastmath=True)
def simulate(L, temperature, num_steps):
    spins = np.ones(shape=(L, L))      
    for step in range(num_steps):
        for _ in range(L*L):
            L = spins.shape[0]
            i = np.random.randint(L)
            j = np.random.randint(L)
            spin = spins[i, j]
            neighbors_sum = spins[(i+1)%L, j] + spins[i, (j+1)%L] + spins[(i-1)%L, j] + spins[i, (j-1)%L]
            energy_diff = 2 * spin * neighbors_sum
            if energy_diff <= 0 or np.random.rand() < np.exp(-energy_diff / temperature):
                spins[i, j] = -spin
    magnetization = np.sum(spins)/(L*L)
    # magnetization = np.mean(spins)
    return magnetization

MC = 10_000  # czas termalizacji, ustawić wyżej!!! (jako MCS)
podział = 30 # podział temperatury
uśrednienia = 100 # ilość trajektorii, z których uśredniany jest wynik

outputs = np.empty(podział)
temp = np.linspace(0.5, 3.5, podział)
#temp = np.concatenate((np.linspace(0.5, 1.85, 12), np.linspace(2, 3, 17), np.linspace(3.1, 3.5, 4)))
t = perf_counter()

markers = ['o', 'D', 'H', '*'] 
L_values = [10,20,40,80]

j = -1
for L in L_values:
    index = 0
    j = j + 1
    for T in temp:
        magnetisation = np.empty(uśrednienia)
        for i in range(uśrednienia):
            magnetisation[i] = simulate(L, T, MC)
        outputs[index] = np.mean(np.abs(magnetisation))
        index += 1
    plt.plot(temp, outputs,label=f'L = {L}', marker = markers[j], linestyle='-')

    
t2 = perf_counter()
print(t2-t)
# plt.ylim([-1.05, 1.05])
plt.xlabel('T*')
plt.ylabel('<m>')
plt.title('Magnetyzacja jako funkcja temperatury (uśrednianie po zespole)')
plt.legend()
plt.savefig('Magnetyzacja jako funkcja temperatury (uśrednianie po zespole)')
plt.show()