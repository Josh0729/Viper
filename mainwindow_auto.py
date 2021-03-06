# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        #MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.timeWidget = QtWidgets.QWidget(self.centralWidget)
        self.timeWidget.setGeometry(QtCore.QRect(210, 170, 381, 141))
        self.timeWidget.setObjectName("timeWidget")
        self.timeDisplay = QtWidgets.QLCDNumber(self.timeWidget)
        self.timeDisplay.setGeometry(QtCore.QRect(-20, 0, 381, 141))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setItalic(True)
        self.timeDisplay.setFont(font)
        self.timeDisplay.setStyleSheet("QLCDNumber{\n"
"    color: rgb(89, 89, 242);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.timeDisplay.setDigitCount(5)
        self.timeDisplay.setObjectName("timeDisplay")
        self.currentWeatherIcon = QtWidgets.QLabel(self.centralWidget)
        self.currentWeatherIcon.setGeometry(QtCore.QRect(40, 20, 131, 91))
        self.currentWeatherIcon.setScaledContents(True)
        self.currentWeatherIcon.setObjectName("currentWeatherIcon")
        self.temperatureLabel = QtWidgets.QLabel(self.centralWidget)
        self.temperatureLabel.setGeometry(QtCore.QRect(170, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.temperatureLabel.setFont(font)
        self.temperatureLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.temperatureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralWidget)
        self.dateLabel.setGeometry(QtCore.QRect(430, 0, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.currentWeatherDescription = QtWidgets.QLabel(self.centralWidget)
        self.currentWeatherDescription.setGeometry(QtCore.QRect(10, 100, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentWeatherDescription.setFont(font)
        self.currentWeatherDescription.setStyleSheet("color: rgb(255, 255, 255);")
        self.currentWeatherDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.currentWeatherDescription.setWordWrap(True)
        self.currentWeatherDescription.setObjectName("currentWeatherDescription")
        self.alarmToolButton = QtWidgets.QToolButton(self.centralWidget)
        self.alarmToolButton.setGeometry(QtCore.QRect(740, 340, 51, 51))
        self.alarmToolButton.setToolTipDuration(-1)
        self.alarmToolButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/alarm-clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.alarmToolButton.setIcon(icon)
        self.alarmToolButton.setIconSize(QtCore.QSize(64, 64))
        self.alarmToolButton.setAutoExclusive(False)
        self.alarmToolButton.setAutoRaise(True)
        self.alarmToolButton.setObjectName("alarmToolButton")
        self.alarmWidget = QtWidgets.QFrame(self.centralWidget)
        self.alarmWidget.setGeometry(QtCore.QRect(490, 310, 300, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarmWidget.sizePolicy().hasHeightForWidth())
        self.alarmWidget.setSizePolicy(sizePolicy)
        self.alarmWidget.setMaximumSize(QtCore.QSize(1000, 111))
        self.alarmWidget.setStyleSheet("")
        self.alarmWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alarmWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.alarmWidget.setLineWidth(1)
        self.alarmWidget.setMidLineWidth(0)
        self.alarmWidget.setObjectName("alarmWidget")
        self.hourListWidget = QtWidgets.QListWidget(self.alarmWidget)
        self.hourListWidget.setGeometry(QtCore.QRect(40, 10, 31, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourListWidget.sizePolicy().hasHeightForWidth())
        self.hourListWidget.setSizePolicy(sizePolicy)
        self.hourListWidget.setMaximumSize(QtCore.QSize(31, 75))
        self.hourListWidget.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.hourListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hourListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hourListWidget.setLineWidth(1)
        self.hourListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hourListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.hourListWidget.setAutoScroll(False)
        self.hourListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.hourListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.hourListWidget.setObjectName("hourListWidget")
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hourListWidget.addItem(item)
        self.minuteListWidget = QtWidgets.QListWidget(self.alarmWidget)
        self.minuteListWidget.setGeometry(QtCore.QRect(80, 10, 31, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minuteListWidget.sizePolicy().hasHeightForWidth())
        self.minuteListWidget.setSizePolicy(sizePolicy)
        self.minuteListWidget.setMaximumSize(QtCore.QSize(31, 75))
        self.minuteListWidget.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.minuteListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minuteListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.minuteListWidget.setLineWidth(1)
        self.minuteListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minuteListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.minuteListWidget.setAutoScroll(False)
        self.minuteListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.minuteListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.minuteListWidget.setSelectionRectVisible(True)
        self.minuteListWidget.setObjectName("minuteListWidget")
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.minuteListWidget.addItem(item)
        self.amPmListWidget = QtWidgets.QListWidget(self.alarmWidget)
        self.amPmListWidget.setGeometry(QtCore.QRect(120, 10, 31, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amPmListWidget.sizePolicy().hasHeightForWidth())
        self.amPmListWidget.setSizePolicy(sizePolicy)
        self.amPmListWidget.setMaximumSize(QtCore.QSize(31, 75))
        self.amPmListWidget.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.amPmListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.amPmListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.amPmListWidget.setLineWidth(1)
        self.amPmListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.amPmListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.amPmListWidget.setAutoScroll(False)
        self.amPmListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.amPmListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.amPmListWidget.setSelectionRectVisible(True)
        self.amPmListWidget.setObjectName("amPmListWidget")
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.amPmListWidget.addItem(item)
        self.alarmOnToolButton = QtWidgets.QToolButton(self.alarmWidget)
        self.alarmOnToolButton.setEnabled(True)
        self.alarmOnToolButton.setGeometry(QtCore.QRect(160, 30, 101, 51))
        self.alarmOnToolButton.setStyleSheet("background-color: transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/ON-switch medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.alarmOnToolButton.setIcon(icon1)
        self.alarmOnToolButton.setIconSize(QtCore.QSize(128, 128))
        self.alarmOnToolButton.setAutoExclusive(False)
        self.alarmOnToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.alarmOnToolButton.setAutoRaise(True)
        self.alarmOnToolButton.setObjectName("alarmOnToolButton")
        self.alarmOffToolButton = QtWidgets.QToolButton(self.alarmWidget)
        self.alarmOffToolButton.setEnabled(True)
        self.alarmOffToolButton.setGeometry(QtCore.QRect(160, 30, 101, 51))
        self.alarmOffToolButton.setStyleSheet("background-color: transparent;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/OFF-switch medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.alarmOffToolButton.setIcon(icon2)
        self.alarmOffToolButton.setIconSize(QtCore.QSize(128, 128))
        self.alarmOffToolButton.setAutoExclusive(False)
        self.alarmOffToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.alarmOffToolButton.setAutoRaise(True)
        self.alarmOffToolButton.setObjectName("alarmOffToolButton")
        self.minuteListWidget.raise_()
        self.hourListWidget.raise_()
        self.amPmListWidget.raise_()
        self.alarmOnToolButton.raise_()
        self.alarmOffToolButton.raise_()
        self.pandoraToolButton = QtWidgets.QToolButton(self.centralWidget)
        self.pandoraToolButton.setGeometry(QtCore.QRect(740, 270, 51, 51))
        self.pandoraToolButton.setToolTipDuration(-1)
        self.pandoraToolButton.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/pandora.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pandoraToolButton.setIcon(icon3)
        self.pandoraToolButton.setIconSize(QtCore.QSize(64, 64))
        self.pandoraToolButton.setAutoExclusive(False)
        self.pandoraToolButton.setAutoRaise(True)
        self.pandoraToolButton.setObjectName("pandoraToolButton")
        self.pandoraWidget = QtWidgets.QFrame(self.centralWidget)
        self.pandoraWidget.setGeometry(QtCore.QRect(490, 240, 251, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pandoraWidget.sizePolicy().hasHeightForWidth())
        self.pandoraWidget.setSizePolicy(sizePolicy)
        self.pandoraWidget.setMaximumSize(QtCore.QSize(1000, 111))
        self.pandoraWidget.setStyleSheet("")
        self.pandoraWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pandoraWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pandoraWidget.setLineWidth(1)
        self.pandoraWidget.setMidLineWidth(0)
        self.pandoraWidget.setObjectName("pandoraWidget")
        self.playToolButton = QtWidgets.QToolButton(self.pandoraWidget)
        self.playToolButton.setEnabled(True)
        self.playToolButton.setGeometry(QtCore.QRect(110, 60, 41, 31))
        self.playToolButton.setStyleSheet("background-color: transparent;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/play_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.playToolButton.setIcon(icon4)
        self.playToolButton.setIconSize(QtCore.QSize(128, 128))
        self.playToolButton.setAutoExclusive(False)
        self.playToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.playToolButton.setAutoRaise(True)
        self.playToolButton.setObjectName("playToolButton")
        self.stopToolButton = QtWidgets.QToolButton(self.pandoraWidget)
        self.stopToolButton.setGeometry(QtCore.QRect(70, 60, 41, 31))
        self.stopToolButton.setStyleSheet("background-color: transparent;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/stop_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.stopToolButton.setIcon(icon5)
        self.stopToolButton.setIconSize(QtCore.QSize(128, 128))
        self.stopToolButton.setAutoExclusive(False)
        self.stopToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.stopToolButton.setAutoRaise(True)
        self.stopToolButton.setObjectName("stopToolButton")
        self.skipToolButton = QtWidgets.QToolButton(self.pandoraWidget)
        self.skipToolButton.setGeometry(QtCore.QRect(150, 60, 41, 31))
        self.skipToolButton.setStyleSheet("background-color: transparent;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/skip_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.skipToolButton.setIcon(icon6)
        self.skipToolButton.setIconSize(QtCore.QSize(128, 128))
        self.skipToolButton.setAutoExclusive(False)
        self.skipToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.skipToolButton.setAutoRaise(True)
        self.skipToolButton.setObjectName("skipToolButton")
        self.pauseToolButton = QtWidgets.QToolButton(self.pandoraWidget)
        self.pauseToolButton.setGeometry(QtCore.QRect(110, 60, 41, 31))
        self.pauseToolButton.setStyleSheet("background-color: transparent;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/pause_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pauseToolButton.setIcon(icon7)
        self.pauseToolButton.setIconSize(QtCore.QSize(128, 128))
        self.pauseToolButton.setAutoExclusive(False)
        self.pauseToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.pauseToolButton.setAutoRaise(True)
        self.pauseToolButton.setObjectName("pauseToolButton")
        self.songLabel = QtWidgets.QLabel(self.pandoraWidget)
        self.songLabel.setGeometry(QtCore.QRect(20, 40, 211, 20))
        self.songLabel.setObjectName("songLabel")
        self.pauseToolButton.raise_()
        self.playToolButton.raise_()
        self.stopToolButton.raise_()
        self.skipToolButton.raise_()
        self.songLabel.raise_()
        self.calendarToolButton = QtWidgets.QToolButton(self.centralWidget)
        self.calendarToolButton.setGeometry(QtCore.QRect(740, 200, 51, 51))
        self.calendarToolButton.setToolTipDuration(-1)
        self.calendarToolButton.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/calendar_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.calendarToolButton.setIcon(icon8)
        self.calendarToolButton.setIconSize(QtCore.QSize(64, 64))
        self.calendarToolButton.setAutoExclusive(False)
        self.calendarToolButton.setAutoRaise(True)
        self.calendarToolButton.setObjectName("calendarToolButton")
        self.calendarWidget = QtWidgets.QFrame(self.centralWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(490, 170, 251, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMaximumSize(QtCore.QSize(1000, 111))
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calendarWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.calendarWidget.setLineWidth(1)
        self.calendarWidget.setMidLineWidth(0)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarLabel = QtWidgets.QLabel(self.calendarWidget)
        self.calendarLabel.setGeometry(QtCore.QRect(5, 5, 300, 90))
        self.calendarLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.calendarLabel.setScaledContents(True)
        self.calendarLabel.setWordWrap(True)
        self.calendarLabel.setObjectName("calendarLabel")
        self.calendarToolButton_2 = QtWidgets.QToolButton(self.centralWidget)
        self.calendarToolButton_2.setGeometry(QtCore.QRect(740, 130, 51, 51))
        self.calendarToolButton_2.setToolTipDuration(-1)
        self.calendarToolButton_2.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.calendarToolButton_2.setIcon(icon9)
        self.calendarToolButton_2.setIconSize(QtCore.QSize(64, 64))
        self.calendarToolButton_2.setAutoExclusive(False)
        self.calendarToolButton_2.setAutoRaise(True)
        self.calendarToolButton_2.setObjectName("calendarToolButton_2")
        self.currentWeatherDescription.raise_()
        self.timeWidget.raise_()
        self.temperatureLabel.raise_()
        self.currentWeatherIcon.raise_()
        self.dateLabel.raise_()
        self.alarmToolButton.raise_()
        self.alarmWidget.raise_()
        self.pandoraToolButton.raise_()
        self.pandoraWidget.raise_()
        self.calendarToolButton.raise_()
        self.calendarWidget.raise_()
        self.calendarToolButton_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Viper"))
        self.currentWeatherIcon.setText(_translate("MainWindow", "TextLabel"))
        self.temperatureLabel.setText(_translate("MainWindow", "--"))
        self.dateLabel.setText(_translate("MainWindow", "--"))
        self.currentWeatherDescription.setText(_translate("MainWindow", "--"))
        self.alarmToolButton.setText(_translate("MainWindow", "..."))
        __sortingEnabled = self.hourListWidget.isSortingEnabled()
        self.hourListWidget.setSortingEnabled(False)
        item = self.hourListWidget.item(2)
        item.setText(_translate("MainWindow", "1"))
        item = self.hourListWidget.item(3)
        item.setText(_translate("MainWindow", "2"))
        item = self.hourListWidget.item(4)
        item.setText(_translate("MainWindow", "3"))
        item = self.hourListWidget.item(5)
        item.setText(_translate("MainWindow", "4"))
        item = self.hourListWidget.item(6)
        item.setText(_translate("MainWindow", "5"))
        item = self.hourListWidget.item(7)
        item.setText(_translate("MainWindow", "6"))
        item = self.hourListWidget.item(8)
        item.setText(_translate("MainWindow", "7"))
        item = self.hourListWidget.item(9)
        item.setText(_translate("MainWindow", "8"))
        item = self.hourListWidget.item(10)
        item.setText(_translate("MainWindow", "9"))
        item = self.hourListWidget.item(11)
        item.setText(_translate("MainWindow", "10"))
        item = self.hourListWidget.item(12)
        item.setText(_translate("MainWindow", "11"))
        item = self.hourListWidget.item(13)
        item.setText(_translate("MainWindow", "12"))
        self.hourListWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.minuteListWidget.isSortingEnabled()
        self.minuteListWidget.setSortingEnabled(False)
        item = self.minuteListWidget.item(2)
        item.setText(_translate("MainWindow", "00"))
        item = self.minuteListWidget.item(3)
        item.setText(_translate("MainWindow", "01"))
        item = self.minuteListWidget.item(4)
        item.setText(_translate("MainWindow", "02"))
        item = self.minuteListWidget.item(5)
        item.setText(_translate("MainWindow", "03"))
        item = self.minuteListWidget.item(6)
        item.setText(_translate("MainWindow", "04"))
        item = self.minuteListWidget.item(7)
        item.setText(_translate("MainWindow", "05"))
        item = self.minuteListWidget.item(8)
        item.setText(_translate("MainWindow", "06"))
        item = self.minuteListWidget.item(9)
        item.setText(_translate("MainWindow", "07"))
        item = self.minuteListWidget.item(10)
        item.setText(_translate("MainWindow", "08"))
        item = self.minuteListWidget.item(11)
        item.setText(_translate("MainWindow", "09"))
        item = self.minuteListWidget.item(12)
        item.setText(_translate("MainWindow", "10"))
        item = self.minuteListWidget.item(13)
        item.setText(_translate("MainWindow", "11"))
        item = self.minuteListWidget.item(14)
        item.setText(_translate("MainWindow", "12"))
        item = self.minuteListWidget.item(15)
        item.setText(_translate("MainWindow", "13"))
        item = self.minuteListWidget.item(16)
        item.setText(_translate("MainWindow", "14"))
        item = self.minuteListWidget.item(17)
        item.setText(_translate("MainWindow", "15"))
        item = self.minuteListWidget.item(18)
        item.setText(_translate("MainWindow", "16"))
        item = self.minuteListWidget.item(19)
        item.setText(_translate("MainWindow", "17"))
        item = self.minuteListWidget.item(20)
        item.setText(_translate("MainWindow", "18"))
        item = self.minuteListWidget.item(21)
        item.setText(_translate("MainWindow", "19"))
        item = self.minuteListWidget.item(22)
        item.setText(_translate("MainWindow", "20"))
        item = self.minuteListWidget.item(23)
        item.setText(_translate("MainWindow", "21"))
        item = self.minuteListWidget.item(24)
        item.setText(_translate("MainWindow", "22"))
        item = self.minuteListWidget.item(25)
        item.setText(_translate("MainWindow", "23"))
        item = self.minuteListWidget.item(26)
        item.setText(_translate("MainWindow", "24"))
        item = self.minuteListWidget.item(27)
        item.setText(_translate("MainWindow", "25"))
        item = self.minuteListWidget.item(28)
        item.setText(_translate("MainWindow", "26"))
        item = self.minuteListWidget.item(29)
        item.setText(_translate("MainWindow", "27"))
        item = self.minuteListWidget.item(30)
        item.setText(_translate("MainWindow", "28"))
        item = self.minuteListWidget.item(31)
        item.setText(_translate("MainWindow", "29"))
        item = self.minuteListWidget.item(32)
        item.setText(_translate("MainWindow", "30"))
        item = self.minuteListWidget.item(33)
        item.setText(_translate("MainWindow", "31"))
        item = self.minuteListWidget.item(34)
        item.setText(_translate("MainWindow", "32"))
        item = self.minuteListWidget.item(35)
        item.setText(_translate("MainWindow", "33"))
        item = self.minuteListWidget.item(36)
        item.setText(_translate("MainWindow", "34"))
        item = self.minuteListWidget.item(37)
        item.setText(_translate("MainWindow", "35"))
        item = self.minuteListWidget.item(38)
        item.setText(_translate("MainWindow", "36"))
        item = self.minuteListWidget.item(39)
        item.setText(_translate("MainWindow", "37"))
        item = self.minuteListWidget.item(40)
        item.setText(_translate("MainWindow", "38"))
        item = self.minuteListWidget.item(41)
        item.setText(_translate("MainWindow", "39"))
        item = self.minuteListWidget.item(42)
        item.setText(_translate("MainWindow", "40"))
        item = self.minuteListWidget.item(43)
        item.setText(_translate("MainWindow", "41"))
        item = self.minuteListWidget.item(44)
        item.setText(_translate("MainWindow", "42"))
        item = self.minuteListWidget.item(45)
        item.setText(_translate("MainWindow", "43"))
        item = self.minuteListWidget.item(46)
        item.setText(_translate("MainWindow", "44"))
        item = self.minuteListWidget.item(47)
        item.setText(_translate("MainWindow", "45"))
        item = self.minuteListWidget.item(48)
        item.setText(_translate("MainWindow", "46"))
        item = self.minuteListWidget.item(49)
        item.setText(_translate("MainWindow", "47"))
        item = self.minuteListWidget.item(50)
        item.setText(_translate("MainWindow", "48"))
        item = self.minuteListWidget.item(51)
        item.setText(_translate("MainWindow", "49"))
        item = self.minuteListWidget.item(52)
        item.setText(_translate("MainWindow", "50"))
        item = self.minuteListWidget.item(53)
        item.setText(_translate("MainWindow", "51"))
        item = self.minuteListWidget.item(54)
        item.setText(_translate("MainWindow", "52"))
        item = self.minuteListWidget.item(55)
        item.setText(_translate("MainWindow", "53"))
        item = self.minuteListWidget.item(56)
        item.setText(_translate("MainWindow", "54"))
        item = self.minuteListWidget.item(57)
        item.setText(_translate("MainWindow", "55"))
        item = self.minuteListWidget.item(58)
        item.setText(_translate("MainWindow", "56"))
        item = self.minuteListWidget.item(59)
        item.setText(_translate("MainWindow", "57"))
        item = self.minuteListWidget.item(60)
        item.setText(_translate("MainWindow", "58"))
        item = self.minuteListWidget.item(61)
        item.setText(_translate("MainWindow", "59"))
        self.minuteListWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.amPmListWidget.isSortingEnabled()
        self.amPmListWidget.setSortingEnabled(False)
        item = self.amPmListWidget.item(2)
        item.setText(_translate("MainWindow", "AM"))
        item = self.amPmListWidget.item(3)
        item.setText(_translate("MainWindow", "PM"))
        self.amPmListWidget.setSortingEnabled(__sortingEnabled)
        self.alarmOnToolButton.setText(_translate("MainWindow", "..."))
        self.alarmOffToolButton.setText(_translate("MainWindow", "..."))
        self.pandoraToolButton.setText(_translate("MainWindow", "..."))
        self.playToolButton.setText(_translate("MainWindow", "..."))
        self.stopToolButton.setText(_translate("MainWindow", "..."))
        self.skipToolButton.setText(_translate("MainWindow", "..."))
        self.pauseToolButton.setText(_translate("MainWindow", "..."))
        self.songLabel.setText(_translate("MainWindow", "TextLabel"))
        self.calendarToolButton.setText(_translate("MainWindow", "..."))
        self.calendarLabel.setText(_translate("MainWindow", "No upcoming events"))
        self.calendarToolButton_2.setText(_translate("MainWindow", "..."))

