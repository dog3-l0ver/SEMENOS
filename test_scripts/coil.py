# Stainless Steel 316L 0.35x3/0.15mm 5 Wrap Alien Coil Test

import numpy as np
import matplotlib.pyplot as plt
import constants as const

# Variables
voltage = 4.2           # V
duration = 5            # s
ambient_temp = 20       # °C
base_temp = 20          # °C
target_temp = 300       # °C

# Calculate resistance of coil at base temperature
base_resistance = const.REF_RES * (1 + const.TEMP_COEFF * (base_temp - const.REF_TEMP))

# Calculate power input in watts
power = voltage**2 / base_resistance

# Calculate heat input in joules
heat = power * duration

# Calculate temperature rise of coil
temp_rise = heat / (const.COIL_MASS * const.HEAT_CAP)

# Calculate total temperature of coil
coil_temp = base_temp + temp_rise

# Calculate resistance of coil at target temperature
target_resistance = const.REF_RES * (1 + const.TEMP_COEFF * (target_temp - const.REF_TEMP))

# Calculate time steps for heating and cooling
steps = 50
time_h = np.linspace(0, duration, steps)
time_c = np.linspace(duration, 2*duration, steps)

# Calculate temperature at each time step for heating and cooling
temp_h = np.zeros(steps)
temp_c = np.zeros(steps)

for i in range(steps):
    temp_h[i] = base_temp + temp_rise * (1 - np.exp(-time_h[i] / (const.COIL_MASS * const.HEAT_CAP)))
    temp_c[i] = coil_temp * np.exp(-(time_c[i] - duration) / (const.COIL_MASS * const.HEAT_CAP))

# Concatenate the two arrays to create the full temperature curve
time = np.concatenate([time_h, time_c])
temp = np.concatenate([temp_h, temp_c])

# Plot the heating and cooling curve
plt.plot(time, temp)
plt.axhline(y=target_temp, color='r', linestyle='--', label='Target Temperature')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Heating and Cooling Curve of Stainless Steel 316L Vape Coil')
plt.legend()
plt.show()
