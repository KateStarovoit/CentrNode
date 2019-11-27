import modules.NodeWrapper as nw
import modules.LoadAnalyzer as la
import flask
import queue
import json
import socket


def getPort():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    the_port = s.getsockname()[1]
    s.close()

    return the_port


def getIp():
    return socket.gethostbyname(socket.gethostname())


Server = flask.Flask(__name__)
ip = getIp()
port = getPort()

file = open("stats.json", "r")
NodeDictList = json.load(file)
NodeDictList.append({"name": socket.gethostname(), "ip": ip, "port": port, "stats": {}})
file.close()

file = open("stats.json", "w")
json.dump(NodeDictList, file, indent=4)
file.close()

node_number = len(NodeDictList)  # temporary
NodeList = []

MessageQueue = queue.Queue()

# TODO Написати нормальний механізм додавання нових нод
for i in range(node_number):
    NodeList.append(nw.NodeWrapper(NodeDictList[i]["name"], NodeDictList[i]["ip"], NodeDictList[i]["port"]))


@Server.route('/send_message/')
def init():
    message = flask.request.json
    MessageQueue.put(message)


# //////////////
# TODO Цей код повинен періодично виконуватись
if NodeList and MessageQueue:
    node_index = la.LoadAnalyzer(NodeList)
    NodeList[node_index].sendMessage(MessageQueue.get())
# //////////////

if __name__ == '__main__':
    Server.run(host=ip, port=port)
