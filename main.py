# always seem to need this
import sys
from time import strftime

# This gets the Qt stuff
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

# This is our window from QtCreator
import mainwindow_auto
from alarm import Alarm
from google_calendar import Calendar
from pandora import Pandora
from weather_conditions import WeatherConditions
from weather_api import WeatherApi
from PyQt5.Qt import QPropertyAnimation, QAbstractItemView,\
    QScrollerProperties, QScroller, QToolButton, QSize

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    CachedWeather = WeatherApi('Initial')
    #AlarmAnimation = QtCore.QPropertyAnimation()
    AlarmInfo = Alarm()
    Pandora = Pandora()
    AlarmCurrentState = 'Closed'
    PandoraCurrentState = 'Closed'
    CalendarCurrentState = 'Closed'
    ANIMATIONDURATION = 650

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.initUI()
        
    def initUI(self):
        self.alarmWidget.setGeometry(QtCore.QRect(800, 310, 300, 100))
        self.pandoraWidget.setGeometry(QtCore.QRect(800, 240, 300, 100))
        self.calendarWidget.setGeometry(QtCore.QRect(800, 170, 300, 100))
        
        self.setupTimers()
        
        self.getTime()
        self.getWeather()
        self.setupScrollers()
        #self.alarmSlider.setStyleSheet(self.styleAlarmSlider())
        self.pauseToolButton.hide()
        self.alarmOnToolButton.hide()
           
        self.setupHooks()
        
        self.hourListWidget.setCurrentRow(2)
        self.minuteListWidget.setCurrentRow(2)
        self.amPmListWidget.setCurrentRow(2)
        
    def setupTimers(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.getTime)
        self.timer.start(10)
        self.alarmTimer = QtCore.QTimer(self)
        self.alarmTimer.timeout.connect(self.checkAlarm)
        self.alarmTimer.start(10)
        self.weatherTimer = QtCore.QTimer(self)
        self.weatherTimer.timeout.connect(self.getWeather)
        self.weatherTimer.start(600000)
        
    def setupHooks(self):
        self.alarmToolButton.clicked.connect(lambda: self.pressedAlarmButton())
        self.hourListWidget.itemSelectionChanged.connect(lambda: self.hourListWidgetSelectionChange())
        self.minuteListWidget.itemSelectionChanged.connect(lambda: self.minuteListWidgetSelectionChange())
        self.amPmListWidget.itemSelectionChanged.connect(lambda: self.amPmListWidgetSelectionChange())
        self.alarmOnToolButton.clicked.connect(lambda: self.pressedAlarmOnButton())
        self.alarmOffToolButton.clicked.connect(lambda: self.pressedAlarmOffButton())
        self.pandoraToolButton.clicked.connect(lambda: self.pressedPandoraButton())
        self.playToolButton.clicked.connect(lambda: self.pressedPlayButton())
        self.pauseToolButton.clicked.connect(lambda: self.pressedPauseButton())
        self.stopToolButton.clicked.connect(lambda: self.pressedStopButton())
        self.skipToolButton.clicked.connect(lambda: self.pressedSkipButton())
        self.calendarToolButton.clicked.connect(lambda: self.pressedCalendarButton())
        
    def setupStatusbar(self):
        self.alarmStatusWidget = QToolButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/alarm-clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.alarmStatusWidget.setIcon(icon)
        self.alarmStatusWidget.setFixedSize(QSize(24,24))
        self.alarmStatusWidget.setIconSize(QSize(24,24))
        
        self.statusBar.setStyleSheet("""QStatusBar::item {
                                        border: none;
                                        }""")

    def setupScrollers(self):
        sp = QScrollerProperties()
        sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.6)
        sp.setScrollMetric(QScrollerProperties.MinimumVelocity, 0.0)
        sp.setScrollMetric(QScrollerProperties.MaximumVelocity, 0.5)
        sp.setScrollMetric(QScrollerProperties.AcceleratingFlickMaximumTime, 0.4)
        sp.setScrollMetric(QScrollerProperties.AcceleratingFlickSpeedupFactor, 1.2)
        sp.setScrollMetric(QScrollerProperties.SnapPositionRatio, 0.2)
        sp.setScrollMetric(QScrollerProperties.MaximumClickThroughVelocity, 0)
        sp.setScrollMetric(QScrollerProperties.DragStartDistance, 0.001)
        sp.setScrollMetric(QScrollerProperties.MousePressEventDelay, 0.5)
        
        hourListScroller = QScroller.scroller(self.hourListWidget) 
        hourListScroller.grabGesture(self.hourListWidget, QScroller.LeftMouseButtonGesture)
        hourListScroller.setScrollerProperties(sp)
        
        minuteListScroller = QScroller.scroller(self.minuteListWidget)
        minuteListScroller.grabGesture(self.minuteListWidget, QScroller.LeftMouseButtonGesture)
        minuteListScroller.setScrollerProperties(sp)
        
        amPmListScroller = QScroller.scroller(self.amPmListWidget)
        amPmListScroller.grabGesture(self.amPmListWidget, QScroller.LeftMouseButtonGesture)
        amPmListScroller.setScrollerProperties(sp)
                
    def getTime(self):
        self.timeDisplay.display(strftime("%I"+":"+"%M").lstrip('0'))
        self.dateLabel.setText(strftime("%A"+" "+"%B"+" "+"%d"+", "+"%Y"))
        
    def getWeather(self):
        successfulResponse = False
        weatherResponse = WeatherApi('Fetch')
        if weatherResponse.response.status_code == 200:
            weatherConditions = WeatherConditions(weatherResponse.response.text)
            successfulResponse = True
        else:
            if self.CachedWeather.response is not None:
                if self.CachedWeather.response.status_code == 200:
                    weatherConditions = WeatherConditions(self.CachedWeather.response.text)
                    successfulResponse = True
        if successfulResponse == True:
            self.currentWeatherIcon.setPixmap(weatherConditions.pixMap)
            self.temperatureLabel.setText(weatherConditions.temperature + u'\u00b0' + 'F')
            self.currentWeatherDescription.setText(weatherConditions.description)
            self.CachedWeather = weatherResponse

    def pressedAlarmButton(self):
        try:
            alarmButtonCurrentGeometry = QtCore.QRect(self.alarmToolButton.geometry())
            alarmButtonAnimation = QPropertyAnimation(self.alarmToolButton,'geometry'.encode(encoding='utf_8'))
            alarmButtonAnimation.setDuration(self.ANIMATIONDURATION)
            alarmButtonAnimation.setStartValue(alarmButtonCurrentGeometry)
            
            alarmWidgetCurrentGeometry = QtCore.QRect(self.alarmWidget.geometry())
            alarmWidgetAnimation = QPropertyAnimation(self.alarmWidget,'geometry'.encode(encoding='utf_8'))
            alarmWidgetAnimation.setDuration(self.ANIMATIONDURATION)
            alarmWidgetAnimation.setStartValue(alarmWidgetCurrentGeometry)
            
            if self.AlarmCurrentState == 'Closed':
                alarmButtonEndTopLeftCorner = QtCore.QPoint(self.alarmToolButton.pos() - QtCore.QPoint(275, 0))
                alarmWidgetEndTopLeftCorner = QtCore.QPoint(self.alarmWidget.pos() - QtCore.QPoint(275, 0))
                self.AlarmCurrentState = 'Open'
            else:
                alarmButtonEndTopLeftCorner = QtCore.QPoint(self.alarmToolButton.pos() + QtCore.QPoint(275, 0))
                alarmWidgetEndTopLeftCorner = QtCore.QPoint(self.alarmWidget.pos() + QtCore.QPoint(275, 0))
                self.AlarmCurrentState = 'Closed'
            
            alarmButtonFinalGeometry = QtCore.QRect(alarmButtonEndTopLeftCorner, QtCore.QSize(self.alarmToolButton.width(), self.alarmToolButton.height()))
            alarmButtonAnimation.setEndValue(alarmButtonFinalGeometry)
            
            alarmWidgetFinalGeometry = QtCore.QRect(alarmWidgetEndTopLeftCorner, QtCore.QSize(self.alarmWidget.width(), self.alarmWidget.height()))
            alarmWidgetAnimation.setEndValue(alarmWidgetFinalGeometry)
            
            alarmButtonAnimation.start()
            alarmWidgetAnimation.start()
            #self.setAlarmWidgetStyleSheet()
            self.AlarmIconAnimation = alarmButtonAnimation
            self.AlarmWidgetAnimation = alarmWidgetAnimation
        except Exception as e:
            print (e.strerror)
            
    def setAlarmWidgetStyleSheet(self):
        style1 = "background-color: white"
        style2 = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))"

        # animation doesn't work for strings but provides an appropriate delay
        animation = QtCore.QPropertyAnimation(self.alarmWidget, 'styleSheet'.encode(encoding='utf_8'))
        animation.setDuration(500)

        state1 = QtCore.QState()
        state2 = QtCore.QState()
        state3 = QtCore.QState()
        state1.assignProperty(self.alarmWidget, 'styleSheet', style1)
        state2.assignProperty(self.alarmWidget, 'styleSheet', style2)
        state3.assignProperty(self.alarmWidget, 'styleSheet', style2)
        #              change a state after an animation has played
        #                               v
        state1.addTransition(state1.propertiesAssigned, state2)
        state2.addTransition(state2.propertiesAssigned, state3)

        self.alarmWidget.machine = QtCore.QStateMachine()
        self.alarmWidget.machine.addDefaultAnimation(animation)
        self.alarmWidget.machine.addState(state1)
        self.alarmWidget.machine.addState(state2)
        self.alarmWidget.machine.setInitialState(state1)
        self.alarmWidget.machine.start()

    def hourListWidgetSelectionChange(self):
        value = self.hourListWidget.currentRow()
        if value < 2:
            value = 2
        if value > 13:
            value = 13
        item = self.hourListWidget.item(value)
        self.hourListWidget.scrollToItem(item,QAbstractItemView.PositionAtCenter)
        self.hourListWidget.setCurrentRow(value)
        
    def minuteListWidgetSelectionChange(self):
        value = self.minuteListWidget.currentRow()
        if value < 2:
            value = 2
        if value > 61:
            value = 61
        item = self.minuteListWidget.item(value)
        self.minuteListWidget.scrollToItem(item,QAbstractItemView.PositionAtCenter)
        self.minuteListWidget.setCurrentRow(value)
        
    def amPmListWidgetSelectionChange(self):
        value = self.amPmListWidget.currentRow()
        if value < 2:
            value = 2
        if value > 3:
            value = 3
        item = self.amPmListWidget.item(value)
        self.amPmListWidget.scrollToItem(item,QAbstractItemView.PositionAtCenter)
        self.amPmListWidget.setCurrentRow(value)
        
    def styleAlarmSlider(self):
        return """
            QSlider::groove:horizontal {
                height: 20px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
                margin: 2px 0;
            }
            
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                    stop: 0 #66e, stop: 1 #bbf);
                background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                    stop: 0 #bbf, stop: 1 #55f);
                height: 40px;
            }

            QSlider::handle:horizontal {
                background: #bbf;
                border: 0px;
                width: 5px;
                margin-top: 0px;
                margin-bottom: 0px;
                border-radius: 0px;
            }
        """
    
#    def alarmSliderValueChange(self):
#        if self.alarmSlider.value() == 0:
#            self.AlarmInfo.disableAlarm()
#        else:
#            hourItem = self.hourListWidget.currentItem()
#            minuteItem = self.minuteListWidget.currentItem()
#            amPmItem = self.amPmListWidget.currentItem()
#            timeToSet = hourItem.text() + ':' + minuteItem.text() + ' ' + amPmItem.text()
#            self.AlarmInfo.setAlarm(timeToSet)
    
    def pressedAlarmOffButton(self):
        self.alarmOffToolButton.hide()
        self.alarmOnToolButton.show()
        hourItem = self.hourListWidget.currentItem()
        minuteItem = self.minuteListWidget.currentItem()
        amPmItem = self.amPmListWidget.currentItem()
        timeToSet = hourItem.text() + ':' + minuteItem.text() + ' ' + amPmItem.text()
        self.AlarmInfo.setAlarm(timeToSet)
        
        self.statusBar.addWidget(self.alarmStatusWidget)
        self.alarmStatusWidget.show()
            
    def pressedAlarmOnButton(self):
        self.alarmOnToolButton.hide()
        self.alarmOffToolButton.show()
        self.AlarmInfo.disableAlarm()
        self.statusBar.removeWidget(self.alarmStatusWidget)
    
    def pressedPandoraButton(self):
        pandoraButtonCurrentGeometry = QtCore.QRect(self.pandoraToolButton.geometry())
        pandoraButtonAnimation = QPropertyAnimation(self.pandoraToolButton,'geometry'.encode(encoding='utf_8'))
        pandoraButtonAnimation.setDuration(self.ANIMATIONDURATION)
        pandoraButtonAnimation.setStartValue(pandoraButtonCurrentGeometry)
            
        pandoraWidgetCurrentGeometry = QtCore.QRect(self.pandoraWidget.geometry())
        pandoraWidgetAnimation = QPropertyAnimation(self.pandoraWidget,'geometry'.encode(encoding='utf_8'))
        pandoraWidgetAnimation.setDuration(self.ANIMATIONDURATION)
        pandoraWidgetAnimation.setStartValue(pandoraWidgetCurrentGeometry)
            
        if self.PandoraCurrentState == 'Closed':
            pandoraButtonEndTopLeftCorner = QtCore.QPoint(self.pandoraToolButton.pos() - QtCore.QPoint(275, 0))
            pandoraWidgetEndTopLeftCorner = QtCore.QPoint(self.pandoraWidget.pos() - QtCore.QPoint(275, 0))
            self.PandoraCurrentState = 'Open'
            if self.Pandora.started == True:
                self.playToolButton.hide()
                self.pauseToolButton.show()
        else:
            pandoraButtonEndTopLeftCorner = QtCore.QPoint(self.pandoraToolButton.pos() + QtCore.QPoint(275, 0))
            pandoraWidgetEndTopLeftCorner = QtCore.QPoint(self.pandoraWidget.pos() + QtCore.QPoint(275, 0))
            self.PandoraCurrentState = 'Closed'
            
        pandoraButtonFinalGeometry = QtCore.QRect(pandoraButtonEndTopLeftCorner, QtCore.QSize(self.pandoraToolButton.width(), self.pandoraToolButton.height()))
        pandoraButtonAnimation.setEndValue(pandoraButtonFinalGeometry)
            
        pandoraWidgetFinalGeometry = QtCore.QRect(pandoraWidgetEndTopLeftCorner, QtCore.QSize(self.pandoraWidget.width(), self.pandoraWidget.height()))
        pandoraWidgetAnimation.setEndValue(pandoraWidgetFinalGeometry)
            
        pandoraButtonAnimation.start()
        pandoraWidgetAnimation.start()
            #self.setpandoraWidgetStyleSheet()
        self.PandoraIconAnimation = pandoraButtonAnimation
        self.PandoraWidgetAnimation = pandoraWidgetAnimation
        
    def pressedPlayButton(self):
        if self.Pandora.started == False:
            self.songLabel.setText('Loading...')
            self.Pandora.start('torkelje@jmu.edu', 'bgc7y9l')
            self.playToolButton.hide()
            self.pauseToolButton.show()
            self.Pandora.read()
            self.songLabel.setText(self.Pandora.output)
        else:
            if self.playToolButton.isvisible():
                self.Pandora.play()
                self.playToolButton.hide()
                self.pauseToolButton.show()
                self.Pandora.read()
                self.songLabel.setText(self.Pandora.output)
            
    def pressedPauseButton(self):
        self.Pandora.pause()
        self.pauseToolButton.hide()
        self.playToolButton.show()
    
    def pressedStopButton(self):
        self.Pandora.stop()
        self.pauseToolButton.hide()
        self.playToolButton.show()
        
    def pressedSkipButton(self):
        self.Pandora.skip()
        
    def checkAlarm(self):
        if self.AlarmInfo.alarmSet == True:
            self.AlarmInfo.checkAlarm()
            if self.AlarmInfo.alarmSet == False:
                self.alarmOnToolButton.hide()
                self.alarmOffToolButton.show()
                #self.pressedPlayButton()
                self.statusBar.removeWidget(self.alarmStatusWidget)
    
    def pressedCalendarButton(self):
        try:
            calendarButtonCurrentGeometry = QtCore.QRect(self.calendarToolButton.geometry())
            calendarButtonAnimation = QPropertyAnimation(self.calendarToolButton,'geometry'.encode(encoding='utf_8'))
            calendarButtonAnimation.setDuration(self.ANIMATIONDURATION)
            calendarButtonAnimation.setStartValue(calendarButtonCurrentGeometry)
            
            calendarWidgetCurrentGeometry = QtCore.QRect(self.calendarWidget.geometry())
            calendarWidgetAnimation = QPropertyAnimation(self.calendarWidget,'geometry'.encode(encoding='utf_8'))
            calendarWidgetAnimation.setDuration(self.ANIMATIONDURATION)
            calendarWidgetAnimation.setStartValue(calendarWidgetCurrentGeometry)
            
            if self.CalendarCurrentState == 'Closed':
                calendarButtonEndTopLeftCorner = QtCore.QPoint(self.calendarToolButton.pos() - QtCore.QPoint(275, 0))
                calendarWidgetEndTopLeftCorner = QtCore.QPoint(self.calendarWidget.pos() - QtCore.QPoint(275, 0))
                self.CalendarCurrentState = 'Open'
                self.Calendar = Calendar()
                self.calendarLabel.setText(self.Calendar.EventList)
            else:
                calendarButtonEndTopLeftCorner = QtCore.QPoint(self.calendarToolButton.pos() + QtCore.QPoint(275, 0))
                calendarWidgetEndTopLeftCorner = QtCore.QPoint(self.calendarWidget.pos() + QtCore.QPoint(275, 0))
                self.CalendarCurrentState = 'Closed'
            
            calendarButtonFinalGeometry = QtCore.QRect(calendarButtonEndTopLeftCorner, QtCore.QSize(self.calendarToolButton.width(), self.calendarToolButton.height()))
            calendarButtonAnimation.setEndValue(calendarButtonFinalGeometry)
            
            calendarWidgetFinalGeometry = QtCore.QRect(calendarWidgetEndTopLeftCorner, QtCore.QSize(self.calendarWidget.width(), self.calendarWidget.height()))
            calendarWidgetAnimation.setEndValue(calendarWidgetFinalGeometry)
            
            calendarButtonAnimation.start()
            calendarWidgetAnimation.start()
            #self.setcalendarWidgetStyleSheet()
            self.CalendarIconAnimation = calendarButtonAnimation
            self.CalendarWidgetAnimation = calendarWidgetAnimation
        except Exception as e:
            print (e.strerror)
        
# main
def main():
    # a new app instance
    app = QApplication(sys.argv)
    main = MainWindow()
#     main.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    main.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())
 
# python bit to figure how who started This
if __name__ == "__main__":
    main()