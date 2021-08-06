import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import sys

# define the initial system state (aka x, y, z positions in space)
initial_state = [0.1, 0, 0]

# define the system parameters sigma, rho, and beta
sigma = float(sys.argv[1])
rho   = float(sys.argv[2])
beta  = float(sys.argv[3])

# define the time points to solve for, evenly spaced between the start and end times
start_time = 1
end_time = 60
interval = 100
time_points = np.linspace(start_time, end_time, end_time * interval)

def lorenz(state, t):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

lorenzsoln = integrate.odeint(lorenz, initial_state, time_points)

fig = plt.figure(figsize=(5, 3))
ax = fig.gca(projection='3d')
x = lorenzsoln[:, 0]
y = lorenzsoln[:, 1]
z = lorenzsoln[:, 2]
ax.plot(x, y, z, color='g', alpha=0.7, linewidth=0.7)

plt.savefig('fig-sigma-'+str(sigma)+'-rho-'+str(rho)+'-beta-'+str(beta)+'.jpg')
