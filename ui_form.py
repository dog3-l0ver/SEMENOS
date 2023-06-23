# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QWidget)
import rc_assets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(360, 720))
        MainWindow.setMaximumSize(QSize(360, 720))
        icon = QIcon()
        icon.addFile(u":/assets/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-image: url(:/assets/background.png);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 360, 720))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.theme_home = QFrame(self.home)
        self.theme_home.setObjectName(u"theme_home")
        self.theme_home.setGeometry(QRect(0, 0, 360, 720))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.theme_home.sizePolicy().hasHeightForWidth())
        self.theme_home.setSizePolicy(sizePolicy1)
        self.theme_home.setBaseSize(QSize(360, 720))
        self.theme_home.setAutoFillBackground(False)
        self.theme_home.setStyleSheet(u"background-image: url(:/assets/home_pink.png);")
        self.theme_home.setFrameShape(QFrame.NoFrame)
        self.theme_home.setFrameShadow(QFrame.Plain)
        self.logo = QFrame(self.theme_home)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(19, 540, 321, 59))
        self.logo.setStyleSheet(u"image: url(:/assets/logo.png);")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Plain)
        self.volts_display = QLabel(self.theme_home)
        self.volts_display.setObjectName(u"volts_display")
        self.volts_display.setGeometry(QRect(185, 249, 131, 91))
        self.volts_display.setAutoFillBackground(False)
        self.volts_display.setStyleSheet(u"font: 60pt \"Motorola ScreenType\";")
        self.volts_display.setFrameShadow(QFrame.Plain)
        self.volts_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.watts_icon = QLabel(self.theme_home)
        self.watts_icon.setObjectName(u"watts_icon")
        self.watts_icon.setGeometry(QRect(280, 144, 51, 81))
        self.watts_icon.setAutoFillBackground(False)
        self.watts_icon.setStyleSheet(u"font: 50pt \"M20_SP-RANKER\";")
        self.watts_icon.setFrameShadow(QFrame.Plain)
        self.watts_icon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_display = QLabel(self.theme_home)
        self.time_display.setObjectName(u"time_display")
        self.time_display.setGeometry(QRect(140, 456, 191, 31))
        font = QFont()
        font.setFamilies([u"Dogica Pixel"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.time_display.setFont(font)
        self.time_display.setAutoFillBackground(False)
        self.time_display.setStyleSheet(u"font: 20pt \"Dogica Pixel\";")
        self.time_display.setFrameShadow(QFrame.Plain)
        self.time_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.battery_display = QLabel(self.theme_home)
        self.battery_display.setObjectName(u"battery_display")
        self.battery_display.setGeometry(QRect(160, 20, 191, 41))
        font1 = QFont()
        font1.setFamilies([u"Retro Gaming"])
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setItalic(False)
        self.battery_display.setFont(font1)
        self.battery_display.setAutoFillBackground(False)
        self.battery_display.setStyleSheet(u"font: 40pt \"Retro Gaming\";")
        self.battery_display.setFrameShadow(QFrame.Plain)
        self.battery_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.puffs_display = QLabel(self.theme_home)
        self.puffs_display.setObjectName(u"puffs_display")
        self.puffs_display.setGeometry(QRect(20, 380, 321, 61))
        font2 = QFont()
        font2.setFamilies([u"Retro Gaming"])
        font2.setPointSize(50)
        font2.setBold(False)
        font2.setItalic(False)
        self.puffs_display.setFont(font2)
        self.puffs_display.setAutoFillBackground(False)
        self.puffs_display.setStyleSheet(u"font: 50pt \"Retro Gaming\";")
        self.puffs_display.setFrameShadow(QFrame.Plain)
        self.puffs_display.setAlignment(Qt.AlignCenter)
        self.version_display = QLabel(self.theme_home)
        self.version_display.setObjectName(u"version_display")
        self.version_display.setGeometry(QRect(20, 615, 321, 31))
        self.version_display.setFont(font)
        self.version_display.setAutoFillBackground(False)
        self.version_display.setStyleSheet(u"font: 20pt \"Dogica Pixel\";")
        self.version_display.setFrameShadow(QFrame.Plain)
        self.version_display.setAlignment(Qt.AlignCenter)
        self.copyright_display = QLabel(self.theme_home)
        self.copyright_display.setObjectName(u"copyright_display")
        self.copyright_display.setGeometry(QRect(20, 660, 321, 31))
        self.copyright_display.setFont(font)
        self.copyright_display.setAutoFillBackground(False)
        self.copyright_display.setStyleSheet(u"font: 20pt \"Dogica Pixel\";")
        self.copyright_display.setFrameShadow(QFrame.Plain)
        self.copyright_display.setAlignment(Qt.AlignCenter)
        self.fire_button = QPushButton(self.theme_home)
        self.fire_button.setObjectName(u"fire_button")
        self.fire_button.setGeometry(QRect(10, 20, 86, 42))
        self.fire_button.setStyleSheet(u"font: 16pt \"Dogica Pixel\";")
        self.fire_button.setIconSize(QSize(0, 0))
        self.fire_button.setFlat(True)
        self.menu_button = QPushButton(self.theme_home)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setGeometry(QRect(107, 20, 86, 42))
        self.menu_button.setStyleSheet(u"font: 16pt \"Dogica Pixel\";")
        self.menu_button.setIconSize(QSize(0, 0))
        self.menu_button.setAutoDefault(False)
        self.menu_button.setFlat(True)
        self.watts_display = QTextEdit(self.theme_home)
        self.watts_display.setObjectName(u"watts_display")
        self.watts_display.setGeometry(QRect(10, 100, 271, 121))
        font3 = QFont()
        font3.setFamilies([u"M20_SP-RANKER"])
        font3.setPointSize(85)
        font3.setBold(False)
        font3.setItalic(False)
        self.watts_display.setFont(font3)
        self.watts_display.setMouseTracking(False)
        self.watts_display.setContextMenuPolicy(Qt.NoContextMenu)
        self.watts_display.setAcceptDrops(False)
        self.watts_display.setStyleSheet(u"font: 85pt \"M20_SP-RANKER\";")
        self.watts_display.setInputMethodHints(Qt.ImhNone)
        self.watts_display.setFrameShape(QFrame.NoFrame)
        self.watts_display.setFrameShadow(QFrame.Plain)
        self.watts_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.watts_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.watts_display.setTabChangesFocus(True)
        self.watts_display.setUndoRedoEnabled(False)
        self.watts_display.setAcceptRichText(False)
        self.watts_display.setTextInteractionFlags(Qt.TextEditable|Qt.TextSelectableByMouse)
        self.ohms_display = QTextEdit(self.theme_home)
        self.ohms_display.setObjectName(u"ohms_display")
        self.ohms_display.setGeometry(QRect(5, 245, 131, 91))
        font4 = QFont()
        font4.setFamilies([u"Motorola ScreenType"])
        font4.setPointSize(60)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.ohms_display.setFont(font4)
        self.ohms_display.setMouseTracking(False)
        self.ohms_display.setContextMenuPolicy(Qt.NoContextMenu)
        self.ohms_display.setAcceptDrops(False)
        self.ohms_display.setStyleSheet(u"font: 60pt \"Motorola ScreenType\";")
        self.ohms_display.setInputMethodHints(Qt.ImhNone)
        self.ohms_display.setFrameShape(QFrame.NoFrame)
        self.ohms_display.setFrameShadow(QFrame.Plain)
        self.ohms_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ohms_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ohms_display.setTabChangesFocus(True)
        self.ohms_display.setUndoRedoEnabled(False)
        self.ohms_display.setOverwriteMode(False)
        self.ohms_display.setAcceptRichText(False)
        self.ohms_display.setTextInteractionFlags(Qt.TextEditable)
        self.stackedWidget.addWidget(self.home)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.theme_menu = QFrame(self.menu)
        self.theme_menu.setObjectName(u"theme_menu")
        self.theme_menu.setGeometry(QRect(0, 0, 360, 720))
        self.theme_menu.setBaseSize(QSize(360, 720))
        self.theme_menu.setAutoFillBackground(False)
        self.theme_menu.setStyleSheet(u"background-image: url(:/assets/menu_pink.png);")
        self.theme_menu.setFrameShape(QFrame.NoFrame)
        self.theme_menu.setFrameShadow(QFrame.Plain)
        self.mode_button = QPushButton(self.theme_menu)
        self.mode_button.setObjectName(u"mode_button")
        self.mode_button.setGeometry(QRect(20, 55, 321, 81))
        self.mode_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.mode_button.setIconSize(QSize(0, 0))
        self.mode_button.setFlat(True)
        self.themes_button = QPushButton(self.theme_menu)
        self.themes_button.setObjectName(u"themes_button")
        self.themes_button.setGeometry(QRect(20, 325, 321, 71))
        self.themes_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.themes_button.setIconSize(QSize(0, 0))
        self.themes_button.setFlat(True)
        self.stats_button = QPushButton(self.theme_menu)
        self.stats_button.setObjectName(u"stats_button")
        self.stats_button.setGeometry(QRect(20, 225, 321, 71))
        self.stats_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.stats_button.setIconSize(QSize(0, 0))
        self.stats_button.setFlat(True)
        self.vapagotchi_button = QPushButton(self.theme_menu)
        self.vapagotchi_button.setObjectName(u"vapagotchi_button")
        self.vapagotchi_button.setGeometry(QRect(20, 425, 321, 71))
        self.vapagotchi_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.vapagotchi_button.setIconSize(QSize(0, 0))
        self.vapagotchi_button.setFlat(True)
        self.back_button = QPushButton(self.theme_menu)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(20, 585, 321, 81))
        self.back_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.back_button.setIconSize(QSize(0, 0))
        self.back_button.setFlat(True)
        self.stackedWidget.addWidget(self.menu)
        self.stats = QWidget()
        self.stats.setObjectName(u"stats")
        self.theme_stats = QFrame(self.stats)
        self.theme_stats.setObjectName(u"theme_stats")
        self.theme_stats.setGeometry(QRect(0, 0, 360, 720))
        self.theme_stats.setStyleSheet(u"background-image: url(:/assets/transparent.png);")
        self.theme_stats.setFrameShape(QFrame.NoFrame)
        self.theme_stats.setFrameShadow(QFrame.Plain)
        self.total_puffs_label = QLabel(self.theme_stats)
        self.total_puffs_label.setObjectName(u"total_puffs_label")
        self.total_puffs_label.setGeometry(QRect(5, 20, 351, 21))
        self.total_puffs_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.total_puffs_label.setAlignment(Qt.AlignCenter)
        self.total_puffs_display = QLabel(self.theme_stats)
        self.total_puffs_display.setObjectName(u"total_puffs_display")
        self.total_puffs_display.setGeometry(QRect(0, 50, 361, 21))
        self.total_puffs_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.total_puffs_display.setAlignment(Qt.AlignCenter)
        self.total_time_label = QLabel(self.theme_stats)
        self.total_time_label.setObjectName(u"total_time_label")
        self.total_time_label.setGeometry(QRect(5, 110, 351, 21))
        self.total_time_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.total_time_label.setAlignment(Qt.AlignCenter)
        self.total_time_display = QLabel(self.theme_stats)
        self.total_time_display.setObjectName(u"total_time_display")
        self.total_time_display.setGeometry(QRect(0, 140, 361, 21))
        self.total_time_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.total_time_display.setAlignment(Qt.AlignCenter)
        self.puff_label = QLabel(self.theme_stats)
        self.puff_label.setObjectName(u"puff_label")
        self.puff_label.setGeometry(QRect(4, 200, 351, 21))
        self.puff_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_label.setAlignment(Qt.AlignCenter)
        self.puff_date_display = QLabel(self.theme_stats)
        self.puff_date_display.setObjectName(u"puff_date_display")
        self.puff_date_display.setGeometry(QRect(0, 230, 361, 21))
        self.puff_date_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_date_display.setAlignment(Qt.AlignCenter)
        self.back_stats = QPushButton(self.theme_stats)
        self.back_stats.setObjectName(u"back_stats")
        self.back_stats.setGeometry(QRect(20, 585, 321, 81))
        self.back_stats.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.back_stats.setIconSize(QSize(0, 0))
        self.back_stats.setFlat(True)
        self.previous_button = QPushButton(self.theme_stats)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setGeometry(QRect(85, 195, 51, 31))
        self.previous_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 15pt \"Dogica Pixel\";")
        self.previous_button.setIconSize(QSize(0, 0))
        self.previous_button.setFlat(True)
        self.next_button = QPushButton(self.theme_stats)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(225, 195, 51, 31))
        self.next_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 15pt \"Dogica Pixel\";")
        self.next_button.setIconSize(QSize(0, 0))
        self.next_button.setFlat(True)
        self.puff_time_label = QLabel(self.theme_stats)
        self.puff_time_label.setObjectName(u"puff_time_label")
        self.puff_time_label.setGeometry(QRect(0, 270, 361, 21))
        self.puff_time_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_time_label.setAlignment(Qt.AlignCenter)
        self.puff_time_display = QLabel(self.theme_stats)
        self.puff_time_display.setObjectName(u"puff_time_display")
        self.puff_time_display.setGeometry(QRect(0, 300, 361, 21))
        self.puff_time_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_time_display.setAlignment(Qt.AlignCenter)
        self.puff_voltage_label = QLabel(self.theme_stats)
        self.puff_voltage_label.setObjectName(u"puff_voltage_label")
        self.puff_voltage_label.setGeometry(QRect(0, 340, 361, 31))
        self.puff_voltage_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_voltage_label.setAlignment(Qt.AlignCenter)
        self.puff_voltage_display = QLabel(self.theme_stats)
        self.puff_voltage_display.setObjectName(u"puff_voltage_display")
        self.puff_voltage_display.setGeometry(QRect(0, 380, 361, 21))
        self.puff_voltage_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_voltage_display.setAlignment(Qt.AlignCenter)
        self.puff_current_label = QLabel(self.theme_stats)
        self.puff_current_label.setObjectName(u"puff_current_label")
        self.puff_current_label.setGeometry(QRect(0, 420, 361, 31))
        self.puff_current_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_current_label.setAlignment(Qt.AlignCenter)
        self.puff_current_display = QLabel(self.theme_stats)
        self.puff_current_display.setObjectName(u"puff_current_display")
        self.puff_current_display.setGeometry(QRect(0, 450, 361, 31))
        self.puff_current_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_current_display.setAlignment(Qt.AlignCenter)
        self.puff_temp_label = QLabel(self.theme_stats)
        self.puff_temp_label.setObjectName(u"puff_temp_label")
        self.puff_temp_label.setGeometry(QRect(0, 500, 361, 31))
        self.puff_temp_label.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_temp_label.setAlignment(Qt.AlignCenter)
        self.puff_temp_display = QLabel(self.theme_stats)
        self.puff_temp_display.setObjectName(u"puff_temp_display")
        self.puff_temp_display.setGeometry(QRect(0, 530, 361, 31))
        self.puff_temp_display.setStyleSheet(u"font: 20pt \"Retro Gaming\";")
        self.puff_temp_display.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.stats)
        self.vapagotchi = QWidget()
        self.vapagotchi.setObjectName(u"vapagotchi")
        self.theme_vapagotchi = QFrame(self.vapagotchi)
        self.theme_vapagotchi.setObjectName(u"theme_vapagotchi")
        self.theme_vapagotchi.setGeometry(QRect(0, 0, 360, 720))
        self.theme_vapagotchi.setStyleSheet(u"background-image: url(:/assets/transparent.png);")
        self.theme_vapagotchi.setFrameShape(QFrame.NoFrame)
        self.theme_vapagotchi.setFrameShadow(QFrame.Plain)
        self.back_vapagotchi = QPushButton(self.theme_vapagotchi)
        self.back_vapagotchi.setObjectName(u"back_vapagotchi")
        self.back_vapagotchi.setGeometry(QRect(20, 585, 321, 81))
        self.back_vapagotchi.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.back_vapagotchi.setIconSize(QSize(0, 0))
        self.back_vapagotchi.setFlat(True)
        self.stackedWidget.addWidget(self.vapagotchi)
        self.themes = QWidget()
        self.themes.setObjectName(u"themes")
        self.theme_themes = QFrame(self.themes)
        self.theme_themes.setObjectName(u"theme_themes")
        self.theme_themes.setGeometry(QRect(0, 0, 360, 720))
        self.theme_themes.setStyleSheet(u"background-image: url(:/assets/themes.png);")
        self.theme_themes.setFrameShape(QFrame.NoFrame)
        self.theme_themes.setFrameShadow(QFrame.Plain)
        self.back_themes = QPushButton(self.theme_themes)
        self.back_themes.setObjectName(u"back_themes")
        self.back_themes.setGeometry(QRect(20, 585, 321, 81))
        self.back_themes.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.back_themes.setIconSize(QSize(0, 0))
        self.back_themes.setFlat(True)
        self.pink_theme_button = QPushButton(self.theme_themes)
        self.pink_theme_button.setObjectName(u"pink_theme_button")
        self.pink_theme_button.setGeometry(QRect(21, 30, 321, 71))
        self.pink_theme_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.pink_theme_button.setIconSize(QSize(0, 0))
        self.pink_theme_button.setFlat(True)
        self.blue_theme_button = QPushButton(self.theme_themes)
        self.blue_theme_button.setObjectName(u"blue_theme_button")
        self.blue_theme_button.setGeometry(QRect(21, 137, 321, 71))
        self.blue_theme_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.blue_theme_button.setIconSize(QSize(0, 0))
        self.blue_theme_button.setFlat(True)
        self.green_theme_button = QPushButton(self.theme_themes)
        self.green_theme_button.setObjectName(u"green_theme_button")
        self.green_theme_button.setGeometry(QRect(21, 244, 321, 71))
        self.green_theme_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.green_theme_button.setIconSize(QSize(0, 0))
        self.green_theme_button.setFlat(True)
        self.red_theme_button = QPushButton(self.theme_themes)
        self.red_theme_button.setObjectName(u"red_theme_button")
        self.red_theme_button.setGeometry(QRect(21, 461, 321, 71))
        self.red_theme_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.red_theme_button.setIconSize(QSize(0, 0))
        self.red_theme_button.setFlat(True)
        self.lavender_theme_button = QPushButton(self.theme_themes)
        self.lavender_theme_button.setObjectName(u"lavender_theme_button")
        self.lavender_theme_button.setGeometry(QRect(21, 353, 321, 71))
        self.lavender_theme_button.setStyleSheet(u"background-image: url(:/assets/background.png);\n"
"font: 700 25pt \"Dogica Pixel\";")
        self.lavender_theme_button.setIconSize(QSize(0, 0))
        self.lavender_theme_button.setFlat(True)
        self.stackedWidget.addWidget(self.themes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.fire_button.setDefault(True)
        self.menu_button.setDefault(True)
        self.mode_button.setDefault(True)
        self.themes_button.setDefault(True)
        self.stats_button.setDefault(True)
        self.vapagotchi_button.setDefault(True)
        self.back_button.setDefault(True)
        self.back_stats.setDefault(True)
        self.previous_button.setDefault(True)
        self.next_button.setDefault(True)
        self.back_vapagotchi.setDefault(True)
        self.back_themes.setDefault(True)
        self.pink_theme_button.setDefault(True)
        self.blue_theme_button.setDefault(True)
        self.green_theme_button.setDefault(True)
        self.red_theme_button.setDefault(True)
        self.lavender_theme_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SEMENOS", None))
        self.volts_display.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.watts_icon.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.time_display.setText(QCoreApplication.translate("MainWindow", u"00.00s", None))
        self.battery_display.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.puffs_display.setText(QCoreApplication.translate("MainWindow", u"000000", None))
        self.version_display.setText(QCoreApplication.translate("MainWindow", u"V 1.0.0", None))
        self.copyright_display.setText(QCoreApplication.translate("MainWindow", u"\u00a92023 CUMS", None))
        self.fire_button.setText(QCoreApplication.translate("MainWindow", u"FIRE", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.watts_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'M20_SP-RANKER'; font-size:85pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">000</p></body></html>", None))
        self.ohms_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Motorola ScreenType'; font-size:60pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.00</p></body></html>", None))
        self.mode_button.setText(QCoreApplication.translate("MainWindow", u"Mode: VW", None))
        self.themes_button.setText(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.stats_button.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.vapagotchi_button.setText(QCoreApplication.translate("MainWindow", u"Vapagotchi", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.total_puffs_label.setText(QCoreApplication.translate("MainWindow", u"Total Puffs:", None))
        self.total_puffs_display.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_time_label.setText(QCoreApplication.translate("MainWindow", u"Total Time:", None))
        self.total_time_display.setText(QCoreApplication.translate("MainWindow", u"0s", None))
        self.puff_label.setText(QCoreApplication.translate("MainWindow", u"Puff:", None))
        self.puff_date_display.setText(QCoreApplication.translate("MainWindow", u"00:00:00 00-00-000", None))
        self.back_stats.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"<=", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"=>", None))
        self.puff_time_label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.puff_time_display.setText(QCoreApplication.translate("MainWindow", u"0s", None))
        self.puff_voltage_label.setText(QCoreApplication.translate("MainWindow", u"Peek Voltage:", None))
        self.puff_voltage_display.setText(QCoreApplication.translate("MainWindow", u"0 V", None))
        self.puff_current_label.setText(QCoreApplication.translate("MainWindow", u"Peek Current:", None))
        self.puff_current_display.setText(QCoreApplication.translate("MainWindow", u"0 A", None))
        self.puff_temp_label.setText(QCoreApplication.translate("MainWindow", u"Peek Temp:", None))
        self.puff_temp_display.setText(QCoreApplication.translate("MainWindow", u"0 C", None))
        self.back_vapagotchi.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.back_themes.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.pink_theme_button.setText(QCoreApplication.translate("MainWindow", u"Pink", None))
        self.blue_theme_button.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.green_theme_button.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.red_theme_button.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.lavender_theme_button.setText(QCoreApplication.translate("MainWindow", u"Lavender", None))
    # retranslateUi
