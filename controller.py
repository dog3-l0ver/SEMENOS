from battery import *
from db import *
import datetime
import threading

class Controller:

    def __init__(self):
        self.battery = Battery()
        self.db = DataBase()
        self.firstRun = [datetime.datetime.today(), datetime.datetime.now().strftime("%H:%M:%S")]

    def thread_management(self):
        t1 = threading.Thread(target=self.battery.simulation())
        t1.start()
        t1.join()
