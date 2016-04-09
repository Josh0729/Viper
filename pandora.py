import requests
import json
import pexpect
from pexpect.popen_spawn import PopenSpawn

class Pandora(object):
    def __init__(self):
        self.started = False
                
    def start(self,user,password):
#523680852782251507
        try:
            #self.pianobarInstance = pexpect.spawn ('pianobar')
            self.pianobarInstance = PopenSpawn ('cmd')
            #self.pianobarInstance.expect('#   -\d\d:\d\d/\d\d:\d\d')
            self.started = True
        except Exception as e:
            print (e.strerror)
        
    def partnerLogin(self):
        partnerLoginData = {
                            "username": "palm",
                            "password": "IUC7IBG09A3JTSYM4N11UJWL07VLH8JP0",
                            "deviceModel": "pre",
                            "version": "5"
                            }
        self.partnerLoginResponse = requests.post('https://tuner.pandora.com/services/json/?method=auth.partnerLogin',json = partnerLoginData)
    
    def userLogin(self,user,password):
        partnerJson = json.loads(self.partnerLoginResponse.text)
        partnerResult = partnerJson['result']
        self.syncTime = partnerResult['syncTime']
        self.partnerAuthToken = partnerResult['partnerAuthToken']
        self.partnerId = partnerResult['partnerId']
        userLoginData = {
                         "loginType": "user",
                         "username": user,
                         "password": password,
                         "partnerAuthToken": self.partnerAuthToken,
                         "includePandoraOneInfo":True,
                         "includeAdAttributes":True,
                         "includeSubscriptionExpiration":True,
                         "includeStationArtUrl":True,
                         "returnStationList":True,
                         "returnGenreStations":True,
                         "syncTime": self.syncTime
                         }
        self.userLoginResponse = requests.post('https://tuner.pandora.com/services/json/?method=auth.userLogin&partner_id='+self.partnerId,json = userLoginData)
        
    def retrieveStations(self):
        userJson = json.loads(self.userLoginResponse.text)
        userResult = userJson['result']
        self.userId = userResult['userId']
        self.userAuthToken = userResult['userAuthToken']
        stationData = {
                       "userAuthToken": self.userAuthToken,
                       "syncTime": self.syncTime
                       }
        self.stationResponse = requests.post('https://tuner.pandora.com/services/json/?method=user.getStationList&partner_id='+self.partnerId+'&user_id='+self.userId, json = stationData)
    
    def retrievePlaylist(self):
        stationJson = json.loads(self.stationResponse.text)
        stationResult = stationJson['result']
        self.stationName = stationResult['stations'][0]['stationName']
        self.stationToken = stationResult['stations'][0]['stationToken']
        playlistData = {
                        "userAuthToken": self.userAuthToken,
                        "additionalAudioUrl":  "HTTP_32_AACPLUS_ADTS,HTTP_64_AACPLUS_ADTS",
                        "syncTime": self.syncTime,
                        "stationToken": self.stationToken
                        }
        self.playlistResponse = requests.post('https://tuner.pandora.com/services/json/?method=station.getPlaylist&partner_id='+self.partnerId+'&user_id='+self.userId, json = playlistData)
    
    def playSong(self):
        playlistJson = json.loads(self.playlistResponse.text)
        playlistResult = playlistJson['result']
        self.song = playlistResult['items'][0]['audioUrlMap']['highQuality']['audioUrl']
        
    def play(self):
        self.pianobarInstance.sendline('p')
        
    def pause(self):
        self.pianobarInstance.sendline('p')
        
    def stop(self):
        self.pianobarInstance.sendline('q')
        self.started = False
        
    def skip(self):
        self.pianobarInstance.sendline('n')
        
    def read(self):
        self.output = self.pianobarInstance.readline()
        
        