import requests
import json


class NodeWrapper:
    def __init__(self, name, ip, port):
        self.__name = name
        self.__ip = ip
        self.__port = port
        self.__stats = {}

    def sendRequest(self, request):
        requests.post("http://" + self.ip + ":" + self.port, data=request)

    def updateStats(self):
        self.stats = requests.post("http://" + self.ip + ":" + self.port)
        # TODO Чекаєм на реалізацію хендлу запиту стати

    def getName(self):
        return self.__name
    
    def getIp(self):
        return self.__ip
    
    def getPort(self):
        return self.__port
                
