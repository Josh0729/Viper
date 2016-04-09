import xml.etree.ElementTree as ET
from PyQt5.Qt import QPixmap
from time import strptime, localtime

class WeatherConditions(object):
    
    def __init__(self,xmlContent):
        self.weatherImage = ''
        self.description = ''
        self.temperature = '--'
        self.root = ET.fromstring(xmlContent)
        self.retrieveWeatherInfo()
    
    def retrieveWeatherInfo(self):
        for currentCondition in self.root.findall('current_condition'):
            currentWeatherCode = currentCondition.find('weatherCode').text
            self.temperature = currentCondition.find('temp_F').text
        for detailDayInfo in self.root.findall('weather'):
            for astronomyInfo in detailDayInfo.findall('astronomy'):
                self.sunrise = strptime(astronomyInfo.find('sunrise').text,"%I:%M %p")
                self.sunset = strptime(astronomyInfo.find('sunset').text,"%I:%M %p")
        self.retrieveConditionInfo(currentWeatherCode)
        self.pixMap = QPixmap(self.weatherImage)
        
    def retrieveConditionInfo(self,conditionCode):
        tree = ET.parse('ConditionCodes.xml')
        root = tree.getroot()
        for condition in root.findall('condition'):
            code = condition.find('code').text
            if code == conditionCode:
                self.description = condition.find('description').text
                if self.sunrise > localtime() or self.sunset < localtime():
                    self.weatherImage = 'images/' + condition.find('night_icon').text
                else:
                    self.weatherImage = 'images/' + condition.find('day_icon').text