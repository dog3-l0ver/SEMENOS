# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from battery import *
from coil import *
from db import *
from time import time
import math
import datetime
import threading


class Controller:
    def __init__(self):
        self.battery = Battery()
        self.db = DataBase()
        battery_cap = self.battery.bat.getcapacity()


    def request_current(self):
        self.battery.bat.setcurrent(self.battery.bat.getcurrent() + 3000)
        self.firstRun = [datetime.datetime.today(), datetime.datetime.now().strftime("%H:%M:%S")]


class MainWindow(QMainWindow):
    date = ''
    mode = 1
    volts = 0
    watts = 0
    current = 0
    resistance = 0
    temperature = 0
    puff_time = 0
    safety_lock = False
    safety_stop = False
    count = False
    id = 1
    i = id
    all_puffs = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_running = True
        self.battery = Battery()
        self.coil = Coil()
        self.resistance = self.coil.get_resitance()
        self.db = DataBase()
        self.battery_cap = self.battery.bat.getcapacity()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.ohms_display.setText(str(self.resistance))
        self.ui.ohms_display.setAlignment(Qt.AlignRight)

        self.ui.menu_button.clicked.connect(self.go_to_menu)
        self.ui.fire_button.pressed.connect(self.fire_start)
        self.ui.fire_button.released.connect(self.fire_stop)

        self.ui.mode_button.clicked.connect(self.set_mode)
        self.ui.stats_button.clicked.connect(self.go_to_stats)
        self.ui.themes_button.clicked.connect(self.go_to_themes)
        self.ui.vapagotchi_button.clicked.connect(self.go_to_vapagotchi)
        self.ui.back_button.clicked.connect(self.go_to_home)

        self.ui.previous_button.clicked.connect(self.previous_stats)
        self.ui.next_button.clicked.connect(self.next_stats)

        self.ui.pink_theme_button.clicked.connect(self.set_theme_pink)
        self.ui.blue_theme_button.clicked.connect(self.set_theme_blue)
        self.ui.green_theme_button.clicked.connect(self.set_theme_green)
        self.ui.lavender_theme_button.clicked.connect(self.set_theme_lavender)
        self.ui.red_theme_button.clicked.connect(self.set_theme_red)
        self.ui.back_themes.clicked.connect(self.go_to_menu)

        self.ui.back_stats.clicked.connect(self.go_to_menu)

        self.ui.back_vapagotchi.clicked.connect(self.go_to_menu)

    def get_capacity(self):
        while(self.is_running):
            battery_left = int(self.battery.bat.getremainingpower() / self.battery_cap * 100)
            self.ui.battery_display.setText(str(battery_left) + "%")


    def thread_start(self):
        self.battery_thread = threading.Thread(target=self.battery.simulation)
        self.battery_thread.start()
        self.capacity_thread = threading.Thread(target=self.get_capacity)
        self.capacity_thread.start()

    def thread_kill(self):
        self.is_running = False
        self.battery.bat.set_status()
        self.db.close_connection()

    def timer(self):
        self.puff_start = time()
        self.count = True
        while self.count:
            self.puff_end = time()
            self.puff_time = self.puff_end - self.puff_start
            self.ui.time_display.setText(str(float('%.2f' % (self.puff_time))) + "s")
            if self.puff_time > 10:
                self.force_stop()

    def go_to_menu(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.menu)

    def go_to_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def go_to_themes(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.themes)

    def go_to_vapagotchi(self):
        level = self.db.total_puffs
        if level < 25:
            self.ui.level_display.setText("Level: " + str(level) + "/25")
        elif level < 50:
            self.ui.level_display.setText("Level: " + str(level) + "/50")
            self.ui.cloudy.setStyleSheet(u"image: url(:/assets/level2.png);")
        else:
            self.ui.level_display.setText("Level: MAX")
            self.ui.cloudy.setStyleSheet(u"image: url(:/assets/level3.png);")
        self.ui.stackedWidget.setCurrentWidget(self.ui.vapagotchi)

    def fire_start(self):
        self.safety_lock = False
        self.safety_stop = False
        match self.mode:
            case 1:
                try:
                    self.watts = int(self.ui.watts_display.toPlainText())
                    self.resistance = float(self.ui.ohms_display.toPlainText())
                    self.volts = math.sqrt(self.watts * self.resistance)
                    self.current = (self.watts / self.volts) * 100
                    if self.volts <= self.battery.bat.getvoltage() and self.current <= 3500:
                        self.ui.volts_display.setText(str(float('%.2f' % (self.volts))))
                        self.timer_thread = threading.Thread(target=self.timer)
                        self.timer_thread.start()
                        self.coil_thread = threading.Thread(target=self.coil.fire, args=(self.watts,))
                        self.coil_thread.start()
                        self.battery.bat.request_current(self.current)

                    else:
                        self.safety_lock = True


                except:
                    pass

            case 2:
                try:
                    self.volts = float(self.ui.watts_display.toPlainText())
                    self.resistance = float(self.ui.ohms_display.toPlainText())
                    self.watts = int((self.volts * self.volts)/self.resistance)
                    self.current = (self.watts / self.volts) * 100
                    if self.volts <= self.battery.bat.getvoltage() and self.current <= 3500:
                        self.ui.volts_display.setText(str(self.watts))
                        self.timer_thread = threading.Thread(target=self.timer)
                        self.timer_thread.start()
                        self.coil_thread = threading.Thread(target=self.coil.fire, args=(self.watts,))
                        self.coil_thread.start()
                        self.battery.bat.request_current(self.current)

                    else:
                        self.safety_lock = True

                except:
                    pass

            case 3:
                pass

    def fire_stop(self):
        self.coil.set_status()
        self.count = False
        self.battery.bat.request_current(0)
        self.temperature = self.coil.get_temp()
        match self.mode:
            case 1:
                self.ui.volts_display.setText("0.00")

            case 2:
                self.ui.volts_display.setText("000")

            case 3:
                pass

        if not self.safety_lock:
            if self.safety_stop == False:
                self.date = str(datetime.datetime.today().replace(microsecond=0))
            self.db.insert_current_puff((self.id, self.date, self.volts, self.current, self.temperature, self.puff_time))
            self.ui.puffs_display.setText(str(self.db.total_puffs).zfill(6))
            self.id += 1

    def force_stop(self):
        self.coil.set_status()
        self.count = False
        self.battery.bat.request_current(0)
        self.safety_stop = True
        self.date = str(datetime.datetime.today().replace(microsecond=0))


    def set_mode(self):
        if(self.mode < 3):
            self.mode += 1

        else:
            self.mode = 1

        match self.mode:
            case 1:
                self.set_mode_vw()

            case 2:
                self.set_mode_vv()

            case 3:
                self.set_mode_tcr()

    def set_mode_vw(self):
        self.ui.mode_button.setText("Mode: VW")
        self.ui.watts_icon.setText("W")
        self.ui.watts_display.setText("000")
        self.ui.watts_display.setAlignment(Qt.AlignRight)
        self.ui.volts_display.setText("0.00")
        self.ui.volts_display.setAlignment(Qt.AlignRight)

    def set_mode_vv(self):
        self.ui.mode_button.setText("Mode: VV")
        self.ui.watts_icon.setText("V")
        self.ui.watts_display.setText("0.00")
        self.ui.watts_display.setAlignment(Qt.AlignRight)
        self.ui.volts_display.setText("000")
        self.ui.watts_display.setAlignment(Qt.AlignRight)

    def set_mode_tcr(self):
        self.ui.mode_button.setText("Mode: TCR")
        self.ui.watts_icon.setText("C")
        self.ui.watts_display.setText("000")
        self.ui.watts_display.setAlignment(Qt.AlignRight)
        self.ui.volts_display.setText("000")
        self.ui.watts_display.setAlignment(Qt.AlignRight)

    def previous_stats(self):
        if self.i > 1:
            self.i -= 1
            current_puff = self.db.select_puff_by_id(self.i)
            self.ui.puff_current_display.setText(str(float('%.2f' % (current_puff[3]/100))) + " A")
            self.ui.puff_date_display.setText(str(current_puff[1]))
            self.ui.puff_temp_display.setText(str(float('%.2f' % (current_puff[4]))) + " C")
            self.ui.puff_time_display.setText(str(float('%.2f' % (current_puff[5]))) + " s")
            self.ui.puff_voltage_display.setText(str(float('%.2f' % (current_puff[2]))) + " V")

    def next_stats(self):
        if self.i < self.id:
            self.i += 1
            current_puff = self.db.select_puff_by_id(self.i)
            self.ui.puff_current_display.setText(str(float('%.2f' % (current_puff[3]/100))) + " A")
            self.ui.puff_date_display.setText(str(current_puff[1]))
            self.ui.puff_temp_display.setText(str(float('%.2f' % (current_puff[4]))) + " C")
            self.ui.puff_time_display.setText(str(float('%.2f' % (current_puff[5]))) + " s")
            self.ui.puff_voltage_display.setText(str(float('%.2f' % (current_puff[2]))) + " V")

    def go_to_stats(self):
        current_puff = self.db.select_latest_puff()
        self.id = current_puff[0]
        self.i = self.id
        self.ui.puff_current_display.setText(str(float('%.2f' % (current_puff[3]/100))) + " A")
        self.ui.puff_date_display.setText(str(current_puff[1]))
        self.ui.puff_temp_display.setText(str(float('%.2f' % (current_puff[4]))) + " C")
        self.ui.puff_time_display.setText(str(float('%.2f' % (current_puff[5]))) + " s")
        self.ui.puff_voltage_display.setText(str(float('%.2f' % (current_puff[2]))) + " V")
        self.ui.total_puffs_display.setText(str(self.db.total_puffs))
        self.ui.total_time_display.setText(str(float('%.2f' % self.db.total_time)) + " s")
        self.ui.stackedWidget.setCurrentWidget(self.ui.stats)

    def set_theme_pink(self):
        self.ui.theme_home.setStyleSheet(u"background-image: url(:/assets/home_pink.png);")
        self.ui.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_pink.png);")

    def set_theme_blue(self):
        self.ui.theme_home.setStyleSheet(u"background-image: url(:/assets/home_blue.png);")
        self.ui.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_blue.png);")

    def set_theme_green(self):
        self.ui.theme_home.setStyleSheet(u"background-image: url(:/assets/home_green.png);")
        self.ui.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_green.png);")

    def set_theme_lavender(self):
        self.ui.theme_home.setStyleSheet(u"background-image: url(:/assets/home_lavender.png);")
        self.ui.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_lavender.png);")

    def set_theme_red(self):
        self.ui.theme_home.setStyleSheet(u"background-image: url(:/assets/home_red.png);")
        self.ui.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_red.png);")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.thread_start()
    app.exec()
    widget.thread_kill()
    sys.exit()
