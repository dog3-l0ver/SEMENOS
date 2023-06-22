# Battery model: 2x Molicel P26A 18650 in series


class BatteryVar:
    def __init__(self):
        # Battery parameters
        self.capacity = 2600  # mAh
        self.remainingpower = 2600  # mAh
        self.base_voltage = 7.4  # V
        self.resistance = 0.4  # Ohm

        # Discharge parameters
        self.current = 150  # mA
        self.dt = 1  # s
        self.voltage = 7.4  # V

    # Getters
    def getcapacity(self):
        return self.capacity

    def getremainingpower(self):
        return self.remainingpower

    def get_base_voltage(self):
        return self.base_voltage

    def getvoltage(self):
        return self.voltage

    def getresistance(self):
        return self.resistance

    def getcurrent(self):
        return self.current

    def getdt(self):
        return self.dt

    # Setters
    def setcapacity(self, capacity):
        self.capacity = capacity

    def setremainingpower(self, remainingpower):
        self.remainingpower = remainingpower

    def setvoltage(self, voltage):
        self.voltage = voltage

    def setresistance(self, resistance):
        self.resistance = resistance

    def setcurrent(self, current):
        self.current = current

    def setdt(self, dt):
        self.dt = dt

    def is_fire(self, isFire, curr):
        if isFire:
            self.setcurrent(500 + curr)
        else:
            self.setcurrent(500)
