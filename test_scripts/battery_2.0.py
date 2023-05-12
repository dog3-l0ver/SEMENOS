# Battery model: Molicel P26A 18650
import math

# Battery parameters
capacity = 2600  # mAh
voltage = 3.7  # V
resistance = 0.002  # Ohms

# Discharge parameters
current = 25  # A
time = 0  # s
dt = 1  # s

# Simulation loop
while capacity > 0:
    # Calculate the voltage across the battery
    v = voltage - current * resistance

    # Calculate the energy discharged in this time step
    energy = current * v * dt / 3600

    # Update the remaining capacity of the battery
    capacity -= energy

    # Update the time
    time += dt

    # Print the remaining capacity and time
    print("Time: {:.1f} s, Capacity: {:.1f} mAh".format(time, capacity))


print("Battery discharged!")
