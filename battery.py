from battery_var import *


class Battery:
    def __init__(self):
        # Battery object
        self.bat = BatteryVar()
        self.time = 0

    def simulation(self):
        while self.bat.getcapacity() > 0:
            # Calculate the voltage across the battery
            v = self.bat.getcurrent() * self.bat.getresistance()

            # Calculate the energy discharged in this time step
            energy = self.bat.getresistance() * self.bat.getcurrent() * v / 36000

            # Update the remaining capacity of the battery
            self.bat.setcapacity(self.bat.getcapacity() - energy)

            # Update the time
            self.time += self.bat.getdt()

            # Print the remaining capacity and time
            print("Time: {:.1f} min, Capacity: {:.1f} mAh".format((self.time / 60), self.bat.getcapacity()))
