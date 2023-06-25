import math
from time import sleep

class Coil:
    def __init__(self):
        self.base_resistance = 0.10              # Ohms
        self.specific_heat_capacity = 100        # J/g·°C
        self.coil_mass = 0.02                    # g
        self.room_temp = 25                      # °C
        self.TCR = 0.000920
        self.k = 5
        self.base_temp = self.room_temp
        self.temp = self.base_temp
        self.resistance = self.base_resistance
        self.peak_temp = self.base_temp
        self.is_fire = False


    # Coil heat up function
    def coil_ramp_up(self, voltage):
        self.temp = self.base_temp
        # Calculate energy lost
        energy = (voltage*self.resistance) * 0.1
        # Calculate temperature change
        temp_change = (energy / (self.coil_mass * self.specific_heat_capacity)) * 50
        self.temp += temp_change
        # Calculate resistance change
        resistance_change = self.base_resistance * self.TCR * temp_change
        self.resistance += resistance_change
        sleep(0.1)


    # Fire function on button press
    def fire(self, voltage):
        self.is_fire = True
        while self.is_fire:
            self.coil_ramp_up(voltage)

        self.peak_temp = self.temp


    # Get coil resistance
    def get_resitance(self):
        return self.resistance

    # Get peak coil temperature
    def get_temp(self):
        return self.peak_temp


    # Switch between heating and cooling
    def set_status(self):
        self.is_fire = False
