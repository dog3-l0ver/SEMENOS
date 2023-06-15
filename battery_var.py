# Battery model: Molicel P26A 18650


class BatteryVar:
    def __init__(self):
        # Battery parameters
        self.capacity = 2600  # mAh
        self.voltage = 3.7  # V
        self.resistance = 0.02  # Ohm

        # Discharge parameters
        self.current = 2000  # Ah
        self.dt = 1  # s

    # Getters
    def getcapacity(self):
        return self.capacity

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

    def setvoltage(self, voltage):
        self.voltage = voltage

    def setresistance(self, resistance):
        self.resistance = resistance

    def setcurrent(self, current):
        self.current = current

    def setdt(self, dt):
        self.dt = dt
