import requests
import json


class NodeWrapper:
    def __init__(self, name, ip, port):
        self.name = str(name)
        self.ip = str(ip)
        self.port = str(port)
        self.stats = {}

    def sendMessage(self, request):
        requests.post("http://" + self.ip + ":" + self.port + "/send_message/", json=request)

    def updateStats(self):
        self.stats = json.loads(requests.post("http://" + self.ip + ":" + self.port + "/get_stats/"))

