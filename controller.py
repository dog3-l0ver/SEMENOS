from battery import *
from db import *
import datetime


class Controller:

    def __init__(self):
        self.battery = Battery()
        self.db = DataBase()
        self.firstRun = [datetime.datetime.today(), datetime.datetime.now().strftime("%H:%M:%S")]

    def thread_management(self):
        self.battery.simulation()
