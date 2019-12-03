import modules.NodeWrapper as nw
import modules.LoadAnalyzer as la
import flask
import requests
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
def add_node():
    content = json.loads(flask.request.json)
    name = content["name"]
    ip = content["ip"]
    port = content["port"]
    NodeList.append(nw.NodeWrapper(name, ip, port))


@Server.route('/send_message/')
def send_message():
    message = flask.request.json
    MessageQueue.put(message)


@Server.route('/create_queue/')
def create_queue():
    content = flask.request.json
    for i in range(len(NodeList)):
        NodeList[i].createQueue(content)


@Server.route('/delete_queue/')
def delete_queue():
    content = flask.request.json
    for i in range(len(NodeList)):
        NodeList[i].deleteQueue(content)


@Server.route('/return_nodes/')
def return_nodes():
    return NodeList


s = sched.scheduler(time.time, time.sleep)


def pullStats():
    # TODO Add timeout
    while True:
        for i in range(len(NodeList)):
            NodeList[i].updateStats()
    # TODO Put stats from all nodes to JSON


def serverRun():
    Server.run(host=ip, port=port)


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=serverRun)
    pullStats_process = multiprocessing.Process(target=pullStats)
    server_process.start()
    pullStats_process.start()
    server_process.join()
    pullStats_process.join()
