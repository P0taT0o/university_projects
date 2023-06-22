# LISTA 8

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
import scipy.stats as stats
import seaborn as sns
sns.set()

# ZADANIE 1

def simulate_markov_chain(x0, P, num_steps):
    num_states = len(P)
    traj = []
    current_state = 1
    traj.append(current_state)
    for _ in range(num_steps-1):
        current_state = np.random.choice(num_states, p=P[current_state])
        traj.append(current_state)
    return traj


x0 = 1  # Stan początkowy
P = np.array([[0.5, 0.5],  # Macierz przejścia
              [1, 0]])
num_steps = 100  # Liczba kroków do symulacji

# Symulacja trajektorii
traj = simulate_markov_chain(x0, P, num_steps)
print(traj)

plt.scatter(range(0,num_steps), traj)
plt.show()

EigenValues, EigenVectors = linalg.eig(P.T)

print("wartosci wlasne:")
print(EigenValues,'\n')
print("wektory wlasne (kolumny macierzy):")
print(EigenVectors*1.5,'\n')

plt.hist(traj, bins = 2, density=True)
plt.show()

def estimate_state_duration(traj):
    state_duration = {}
    current_state = traj[0]
    duration = 1

    for state in traj[1:]:
        if state == current_state:
            duration += 1
        else:
            if current_state in state_duration:
                state_duration[current_state].append(duration)
            else:
                state_duration[current_state] = [duration]
            duration = 1
            current_state = state

    if current_state in state_duration:
        state_duration[current_state].append(duration)
    else:
        state_duration[current_state] = [duration]

    return state_duration

# Oszacowanie czasu przebywania w poszczególnych stanach
state_duration = estimate_state_duration(traj)

# Wyświetlanie wyników
for state, durations in state_duration.items():
    total_duration = sum(durations)
    state_percentage = (total_duration / num_steps) * 100
    print(f"Stan {state}: Czas przebywania = {total_duration} ({state_percentage:.2f}%)")
    
# inny przykład

x0 = 1  
P = np.array([[0, 0.5, 0.5],  
              [0.5, 0.5, 0],
              [0.5, 0.5, 0]])
num_steps = 100  

traj = simulate_markov_chain(x0, P, num_steps)
print(traj)

plt.scatter(range(0,num_steps), traj)
plt.show()

EigenValues, EigenVectors = linalg.eig(P.T)

print("wartosci wlasne:")
print(EigenValues,'\n')
print("wektory wlasne (kolumny macierzy):")
print(EigenVectors*1.5,'\n')

plt.hist(traj, bins = 3, density=True)
plt.show()

state_duration = estimate_state_duration(traj)

for state, durations in state_duration.items():
    total_duration = sum(durations)
    state_percentage = (total_duration / num_steps) * 100
    print(f"Stan {state}: Czas przebywania = {total_duration} ({state_percentage:.2f}%)")
    
    
# ZADANIE 2

def generate_continuous_markov_chain(x0, P, lambdas, max_time):
    num_states = len(P)
    traj = []
    states = []
    ts = []
    current_state = x0
    traj.append((current_state, 0))

    t = 0
    while t < max_time:
        state = traj[-1][0]
        intensity = lambdas[state]
        duration = stats.expon(scale=1/intensity).rvs()
        t += duration

        if t > max_time:
            break

        current_state = np.random.choice(num_states, p=P[state])
        traj.append((current_state, t))

    for state, t in traj:
        states.append(state)
        ts.append(t)

    return states, ts

x0 = 0 # Stan początkowy
P = np.array([[0, 1],  # Macierz przejścia
              [1, 0]])
lambdas = [1, 2]  # Funkcje intensywności
max_time = 50.0  # Maksymalny czas trajektorii

# Generowanie trajektorii
states, ts = generate_continuous_markov_chain(x0, P, lambdas, max_time)
# print(states)
# print(ts)

plt.step(ts, states)
plt.show()

plt.hist(states, bins=2, density=True)
plt.show()
