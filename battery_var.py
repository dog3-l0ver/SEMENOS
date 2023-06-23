# Battery model: 2x Molicel P26A 18650 in series


class BatteryVar:
    def __init__(self):
        # Battery parameters
        self.capacity = 2600        # mAh
        self.remainingpower = 2600  # mAh
        self.base_voltage = 7.4     # V
        self.resistance = 0.4       # Ohm

        # Discharge parameters
        self.current = 150          # mA
        self.requested_current = 0  # mA
        self.voltage = 7.4          # V
        self.is_running = True

    # Getters
    def get_requested_current(self):
        return self.requested_current

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

    def get_status(self):
        return self.is_running

    # Setters
    def request_current(self, requested_current):
        self.requested_current = requested_current

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

    def set_status(self):
        self.is_running = False
