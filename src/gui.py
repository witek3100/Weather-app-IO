from PyQt5 import QtCore, QtGui, QtWidgets
from weather_data_request import WeatherApi
from location_request import LocationApi
import time
import os
import json
import requests
import re
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 719)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 112, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(30, 100, 190);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.city_label = QtWidgets.QLabel(self.centralwidget)
        self.city_label.setGeometry(QtCore.QRect(400, 60, 191, 81))
        self.city_label.setStyleSheet("font: 700 30pt \"Calibri\";\n"
"background-color: rgba(191, 64, 64, 2);\n"
"color: rgb(243, 243, 243);")
        self.city_label.setObjectName("city_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 1001, 51))
        self.label_2.setStyleSheet("background-color:rgb(30, 100, 190)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.pushButton.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.reload_location())
        self.pushButton_2.setGeometry(QtCore.QRect(140, 10, 121, 31))
        self.pushButton_2.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.update_weather())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.pushButton_3.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QTextEdit(self.centralwidget, placeholderText=" search city")
        self.lineEdit.setGeometry(QtCore.QRect(650, 10, 291, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(130,200,250)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: update_city())
        self.pushButton_4.setGeometry(QtCore.QRect(950, 10, 31, 31))
        self.pushButton_4.setStyleSheet("background-color:rgb(100,200,250)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.current_location_label = QtWidgets.QLabel(self.centralwidget)
        self.current_location_label.setGeometry(QtCore.QRect(0, 700, 991, 21))
        self.current_location_label.setStyleSheet("background-color:rgba(30, 100, 190, 100);\n"
                                   "font: 300 9pt \"Bahnschrift Light\";")
        self.current_location_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.current_location_label.setObjectName("label_4")

        self.temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label.setGeometry(QtCore.QRect(370, 130, 221, 101))
        self.temperature_label.setStyleSheet("font: 300 50pt \"Segoe UI Variable Display Light\";\n"
                                             "color:rgb(255,255,255)")
        self.temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature_label.setObjectName("temperature_label")

        self.wth = QtWidgets.QLabel(self.centralwidget)
        self.wth.setGeometry(QtCore.QRect(360, 240, 251, 41))
        self.wth.setStyleSheet("font: 20pt \"Calibri\";\n"
                               "color:rgb(255, 255, 255)")
        self.wth.setAlignment(QtCore.Qt.AlignCenter)
        self.wth.setObjectName("wth")

        self.current_data_label1 = QtWidgets.QLabel(self.centralwidget)
        self.current_data_label1.setGeometry(QtCore.QRect(250, 320, 461, 31))
        self.current_data_label1.setStyleSheet("color:rgb(255, 255, 255)")
        self.current_data_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.current_data_label1.setObjectName("current_data_label1")

        self.current_data_label2 = QtWidgets.QLabel(self.centralwidget)
        self.current_data_label2.setGeometry(QtCore.QRect(250, 290, 461, 31))
        self.current_data_label2.setStyleSheet("color:rgb(255, 255, 255)")
        self.current_data_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.current_data_label2.setObjectName("current_data_label2")

        self.actionChange_units = QtWidgets.QAction(MainWindow)
        self.actionChange_units.setObjectName("actionChange_units")
        self.actiontime_zone = QtWidgets.QAction(MainWindow)
        self.actiontime_zone.setObjectName("actiontime_zone")

        ##### FORECAST #####
        self.frcs_label = QtWidgets.QLabel(self.centralwidget)
        self.frcs_label.setGeometry(QtCore.QRect(50, 410, 891, 221))
        self.frcs_label.setStyleSheet("background-color:rgba(30, 100, 190, 150);\n"
                                      "font: 300 9pt \"Bahnschrift Light\";\n"
                                      "border-radius:20px;")
        self.frcs_label.setText("")
        self.frcs_label.setObjectName("frcs_label")

        self.h_temperature_2 = QtWidgets.QLabel(self.centralwidget)
        self.h_temperature_2.setGeometry(QtCore.QRect(150, 510, 741, 20))
        self.h_temperature_2.setStyleSheet("font: 700 9pt \"Segoe UI\";"
                                           "color: rgb(255,255,255)")
        self.h_temperature_2.setObjectName("h_temperature_2")
        self.hours_2 = QtWidgets.QLabel(self.centralwidget)
        self.hours_2.setGeometry(QtCore.QRect(130, 530, 811, 20))
        self.hours_2.setStyleSheet("color:rgb(255,255,255);")
        self.hours_2.setObjectName("hours_2")

        self.Hourly_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_hourly_forecast())
        self.Hourly_button.setGeometry(QtCore.QRect(60, 470, 83, 29))
        self.Hourly_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.Hourly_button.setObjectName("Hourly_button")
        self.Daily_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.show_daily_forecast())
        self.Daily_button.setGeometry(QtCore.QRect(60, 510, 83, 29))
        self.Daily_button.setStyleSheet("background-color:rgb(100,200,250)")
        self.Daily_button.setObjectName("Daily_button")

        self.dates_2 = QtWidgets.QLabel(self.centralwidget)
        self.dates_2.setGeometry(QtCore.QRect(130, 530, 738, 20))
        self.dates_2.setStyleSheet("color:rgb(255,255,255);")
        self.dates_2.setObjectName("dates_2")
        self.max_temperature_2 = QtWidgets.QLabel(self.centralwidget)
        self.max_temperature_2.setGeometry(QtCore.QRect(160, 510, 741, 20))
        self.max_temperature_2.setStyleSheet("font: 700 9pt \"Segoe UI\";"
                                             "color: rgb(255,255,255)")
        self.max_temperature_2.setObjectName("max_temperature_2")
        self.min_temperature_2 = QtWidgets.QLabel(self.centralwidget)
        self.min_temperature_2.setGeometry(QtCore.QRect(180, 510, 741, 20))
        self.min_temperature_2.setStyleSheet("font:10pt \"Calibri\";\n"
                                             "color:rgb(172, 172, 172)")
        self.min_temperature_2.setObjectName("min_temperature_2")
        self.min_4 = QtWidgets.QLabel(self.centralwidget)
        self.min_4.setGeometry(QtCore.QRect(900, 500, 63, 21))
        self.min_4.setStyleSheet("font:9pt \"Calibri\";\n"
                                 "color:rgb(172, 172, 172)")
        self.min_4.setObjectName("min_4")
        self.max = QtWidgets.QLabel(self.centralwidget)
        self.max.setGeometry(QtCore.QRect(900, 520, 63, 21))
        self.max.setStyleSheet("font: 700 7pt \"Segoe UI\";"
                               "color: rgb(255, 255, 255)")
        self.max.setObjectName("max")

        self.forecast = QtWidgets.QLabel(self.centralwidget)
        self.forecast.setGeometry(QtCore.QRect(60, 430, 101, 31))
        self.forecast.setStyleSheet("font: 15pt \"Calibri\";\n"
                                    "color:rgb(255, 255, 255)")
        self.forecast.setObjectName("forecast")
        self.frcs_label.raise_()
        self.hours_2.raise_()
        self.h_temperature_2.raise_()
        self.forecast.raise_()
        self.city_label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lineEdit.raise_()
        self.pushButton_4.raise_()
        self.temperature_label.raise_()
        self.wth.raise_()
        self.dates_2.raise_()
        self.max_temperature_2.raise_()
        self.min_temperature_2.raise_()
        self.min_4.raise_()
        self.max.raise_()
        self.current_data_label1.raise_()
        self.current_data_label2.raise_()
        self.Hourly_button.raise_()
        self.Daily_button.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_city(self):
        self.label.setText(self.lineEdit.toPlainText())

    def update_weather(self):
        WeatherApi.get_weather()
        with open(os.path.relpath("weather_data.json")) as wth_file:
            self.weather = json.load(wth_file)
        t = time.localtime()
        hour = int(time.strftime("%H", t))

        #set temperature label
        self.temperature_label.setText("{}°C".format(self.weather["hourly"]["temperature_2m"][hour]))

        #set wth label and main icon
        clouds = self.weather["hourly"]["cloudcover"][hour]
        if 0 <= clouds < 10:
            self.wth.setText("Clear sky")
        elif 10 <= clouds < 30:
            self.wth.setText("Mostly clear")
        elif 30 <= clouds < 60:
            self.wth.setText("Partly clear")
        elif 60 <= clouds < 95:
            self.wth.setText("Broken clouds")
        elif 95 <= clouds <= 100:
            self.wth.setText("Overcast")
        rain = self.weather["hourly"]["rain"][hour]
        percipation = 0
        if rain > 0:
            self.wth.setText("Rain")
            percipation = rain
        snow = self.weather["hourly"]["snowfall"][hour]
        if snow > 0:
            self.wth.setText("Snow")
            percipation = snow

        #set current_data_label1
        feels_like = self.weather["hourly"]["apparent_temperature"][hour]
        humidity = self.weather["hourly"]["relativehumidity_2m"][hour]
        self.current_data_label2.setText("Feels Like {}°C      Precipitation {} mm       Humidity {}%".format(feels_like, percipation, humidity))

        #set current_data_label2
        wind = self.weather["hourly"]["windspeed_10m"][hour]
        visibility = self.weather["hourly"]["visibility"][hour]
        barometer = self.weather["hourly"]["pressure_msl"][hour]
        self.current_data_label1.setText("Wind  {} km/h       Visibility {} m       Barometer {} hPa".format(wind, visibility, barometer))

    def reload_location(self):
        try:
            LocationApi.get_location()
            with open(os.path.relpath("loc.json")) as loc_file:
                loc = json.load(loc_file)
                self.lat = loc["results"][1]['geometry']['location']['lat']
                self.lon = loc["results"][1]['geometry']['location']['lng']
        except:
            self.current_location_label.setText("UNABLE TO GET YOUR LOCATION")
        else:
            self.current_location_label.setText("CURRENT LOCATION: {}   {}".format(self.lat, self.lon))

    def show_daily_forecast(self):
        #hide hourly
        self.hours_2.hide()
        self.h_temperature_2.hide()
        #display daily
        self.max.show()
        self.min_4.show()
        self.dates_2.show()
        self.min_temperature_2.show()
        self.max_temperature_2.show()


    def show_hourly_forecast(self):
        #hide daily
        self.max.hide()
        self.min_4.hide()
        self.dates_2.hide()
        self.min_temperature_2.hide()
        self.max_temperature_2.hide()
        #show hourly
        self.hours_2.show()
        self.h_temperature_2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.city_label.setText(_translate("MainWindow", "Kraków"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.pushButton_2.setText(_translate("MainWindow", "Reload location"))
        self.pushButton_3.setText(_translate("MainWindow", "Update Weather"))
        self.current_location_label.setText(_translate("MainWindow", "CURRENT LOCATION: "))
        self.actionChange_units.setText(_translate("MainWindow", "Units"))
        self.actiontime_zone.setText(_translate("MainWindow", "Time zone"))
        self.temperature_label.setText(_translate("MainWindow", "28°C"))
        self.wth.setText(_translate("MainWindow", "Partly Sunny"))
        self.current_data_label1.setText(
            _translate("MainWindow", "Wind  se 10ms       Visibility 10km       Barometer 1013 hpa"))
        self.current_data_label2.setText(
            _translate("MainWindow", "Feels Like 24°C      Precipitation None        Humidity 80%"))
        self.actionChange_units.setText(_translate("MainWindow", "Units"))
        self.actiontime_zone.setText(_translate("MainWindow", "Time zone"))
        self.forecast.setText(_translate("MainWindow", "Forecast"))
        self.Hourly_button.setText(_translate("MainWindow", "Hourly"))
        self.Daily_button.setText(_translate("MainWindow", "Daily"))
        self.h_temperature_2.setText(_translate("MainWindow",
                                                "             4°C                         4°C                        4°C                         4°C                          4°C                         4°C"))
        self.hours_2.setText(_translate("MainWindow",
                                        "                  3:00                        7:00                       11:00                       15:00                       19:00                       23:00"))
        self.dates_2.setText(_translate("MainWindow",
                                        "                 30.12                       31.12                       01.01                       02.01                       03.01                       04.01"))
        self.max_temperature_2.setText(_translate("MainWindow",
                                                  "              4°C                         4°C                          4°C                          4°C                          4°C                          4°C"))
        self.min_temperature_2.setText(_translate("MainWindow",
                                                  "1°C                          1°C                          1°C                          1°C                          1°C                          1°C   "))
        self.min_4.setText(_translate("MainWindow", "MIN"))
        self.max.setText(_translate("MainWindow", "MAX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.reload_location()
    ui.update_weather()
    ui.show_daily_forecast()
    MainWindow.show()
    sys.exit(app.exec_())