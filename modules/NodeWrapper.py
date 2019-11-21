import requests
import json


class NodeWrapper:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.stats = {}

    def sendRequest(self, request):
        requests.post("http://" + self.ip + ":" + self.port, data=request)

    def updateStats(self):
        self.stats = requests.post("http://" + self.ip + ":" + self.port)
        # TODO Чекаєм на реалізацію хендлу запиту стати

    