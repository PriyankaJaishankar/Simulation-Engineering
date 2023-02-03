import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the parameters
r1 = 0
r2 = 0
v1 = 0.5
v2 = 0.5
w = 0.75

# Define the differential equations
def two_tank_system(x, t):
    dxdt = np.zeros(2)
    if x[0] > r1:
        dxdt[0] = w - v1
    else:
        dxdt[0] = 0
    if x[1] > r2:
        dxdt[1] = w - v2
    else:
        dxdt[1] = 0
    return dxdt

# Set the initial conditions
x0 = [0, 1]

# Simulate the system for 100 seconds
t = np.linspace(0, 100, 1000)
x = odeint(two_tank_system, x0, t)

# Plot the results
plt.plot(t, x[:,0], '-b', linewidth=2)
plt.plot(t, x[:,1], '-r', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Volume of Water')
plt.legend(['Tank 1', 'Tank 2'])
plt.show()
