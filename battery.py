import datetime
from time import sleep
from battery_var import *


class Battery:
    def __init__(self):
        # Battery object
        self.bat = BatteryVar()
        self.time = 0

    def simulation(self):
        i = 0
        data = []
        while self.bat.getremainingpower() > 0:
            # Calculate the voltage across the battery
            v = self.bat.getcurrent() * self.bat.getresistance()

            # Calculate the energy discharged in this time step
            energy = self.bat.getresistance() * self.bat.getcurrent() * v / 3600

            # Update the remaining capacity of the battery
            self.bat.setremainingpower(self.bat.getremainingpower() - energy)

            # Update the time
            self.time += self.bat.getdt()

            remainingpower = [(self.bat.getremainingpower() / self.bat.getcapacity()) * 100,
                              self.time / 60,
                              datetime.date.today(),
                              datetime.datetime.now().strftime("%H:%M:%S")]

            data.append(remainingpower)

            # Print the remaining capacity and time
            print("Capacity: {:.0f}%, Time: {:.1f} min, Timestamp: {ftstamp}".format(data[i][0], data[i][1],
                                                                                     ftstamp=str(
                                                                                         data[i][2]) + " " + str(
                                                                                         data[i][3])))

            if data[i][0] < 1:
                break
            i += 1
            sleep(0.1)
