import modules.NodeWrapper as nw
import modules.LoadAnalyzer as la
import flask
import queue
import multiprocessing
import time
import sched
import json

Server = flask.Flask(__name__)
ip = "localhost"
port = "8888"

NodeList = []

MessageQueue = queue.Queue(maxsize=100)


@Server.route('/add_node/')
def init():
    content = json.loads(flask.request.json)
    name = content["name"]
    ip = content["ip"]
    port = content["port"]
    NodeList.append(nw.NodeWrapper(name, ip, port))


@Server.route('/send_message/')
def init():
    message = flask.request.json
    MessageQueue.put(message)


@Server.route('/login/')
def check_login():
    login_base = json.load(open ("login_database.json"))
    content = json.loads(flask.request.json)
    if content["login"] in login_base:
        return True
    else:
        return False





s = sched.scheduler(time.time, time.sleep)


def pullStats():
    while True:
        if len(NodeList) > 0 and MessageQueue.qsize() > 0:
            node_index = la.LoadAnalyzer(NodeList)
            NodeList[node_index].sendMessage(MessageQueue.get())


def serverRun():
    Server.run(host=ip, port=port)


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=serverRun)
    pullStats_process = multiprocessing.Process(target=pullStats)
    server_process.start()
    pullStats_process.start()
    server_process.join()
    pullStats_process.join()
