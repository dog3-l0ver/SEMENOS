import numpy as np
from scipy.integrate import odeint

# Battery parameters
C = 2500.0  # mAh
R = 0.05  # Ohm

# Constants
V0 = 4.2  # V, fully charged voltage
Q = C * 3600 / 1000  # As, battery capacity
I0 = 0.5  # A, initial discharge current

# Time range for simulation
t0 = 0  # s, initial time
t_end = 3000  # s, end time
n = 1000  # number of time points
t = np.linspace(t0, t_end, n)

# Function for battery discharge process
def discharge(y, t):
    V = y[0]
    I = y[1]
    Q_remaining = y[2]
    dVdt = -I * R / Q_remaining
    dIdt = -I / (R * C) * V
    dQdt = -I / 3600
    return [dVdt, dIdt, dQdt]

# Initial conditions
y0 = [V0, I0, Q]

# Solve the differential equation
sol = odeint(discharge, y0, t)

# Extract the solution
V = sol[:, 0]
I = sol[:, 1]
Q_remaining = sol[:, 2]

# Update the values of voltage, current, and remaining capacity
for i in range(1, n):
    dt = t[i] - t[i-1]
    V[i] = V[i-1] + discharge([V[i-1], I[i-1], Q_remaining[i-1]], t[i])[0] * dt
    I[i] = I[i-1] + discharge([V[i-1], I[i-1], Q_remaining[i-1]], t[i])[1] * dt
    Q_remaining[i] = Q_remaining[i-1] + discharge([V[i-1], I[i-1], Q_remaining[i-1]], t[i])[2] * dt

# Print the results
print("Time (s)\tVoltage (V)\tCurrent (A)\tCapacity (mAh)")
for i in range(len(t)):
    # Print results
    print(f"{t[i]:.2f}\t\t{V[i]:.2f}\t\t{I[i]:.2f}\t\t{Q_remaining[i]/3600:.2f}")