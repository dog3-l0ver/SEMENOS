from battery import *
from battery_var import *


class Controller:

    def __init__(self):
        self.battery = Battery()
        self.battery_var = BatteryVar()

    def threadmanagement(self):
        self.battery.simulation()
