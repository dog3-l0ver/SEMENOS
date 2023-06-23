import datetime
from time import sleep
from battery_var import *


class Battery:
    def __init__(self):
        # Battery object
        self.bat = BatteryVar()

    def simulation(self):
        while self.bat.getremainingpower() > 0 and self.bat.get_status():
            # Calculate the voltage across the battery
            self.bat.setvoltage(self.bat.get_base_voltage() * ((self.bat.getremainingpower() + (5 * self.bat.getcapacity())) / (self.bat.getcapacity() * 6)))

            # Calculate the energy discharged in this time step
            energy = self.bat.getresistance() * (self.bat.getcurrent() + self.bat.get_requested_current()) * self.bat.getvoltage() / 3600

            # Update the remaining capacity of the battery
            self.bat.setremainingpower(self.bat.getremainingpower() - energy)

            sleep(0.1)
