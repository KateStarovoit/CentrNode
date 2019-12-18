import os
import modules.NodeWrapper as nw
import flask
from flask import request, render_template
import requests
import queue
import multiprocessing
import time
import sched
import json

from utils import get_statistics

Server = flask.Flask(__name__)
ip = "localhost"
port = "8888"

NodeList = []
MessageQueue = queue.Queue(maxsize=100)


@Server.route('/add_node/')
def add_node():
    content = json.loads(flask.request.json)
    name = content["name"]
    ip_address = content["ip"]
    new_port = content["port"]
    NodeList.append(nw.NodeWrapper(name, ip_address, new_port))


@Server.route('/send_message/')
def send_message():
    message = flask.request.json
    MessageQueue.put(message)


@Server.route('/create_queue/')
def create_queue():
    content = flask.request.json
    content = json.load(content)
    names = json.load("queue_names.json")
    names.append(content["name"])

    for i in range(len(NodeList)):
        NodeList[i].createQueue(content)


@Server.route('/delete_queue/')
def delete_queue():
    content = flask.request.json
    
    content = json.load(content)
    file = open("queue_names.json")
    names = json.load(file)
    file.close()

    for i in range(len(names)):
        if names[i] == content["name"]:
            names.pop(i)
            break

    for i in range(len(NodeList)):
        NodeList[i].deleteQueue(content)


@Server.route('/return_nodes/')
def return_nodes():
    return NodeList

s = sched.scheduler(time.time, time.sleep)

def pullStats():
    # TODO Add timeout
    file = open("stats.json")
    stats = json.load(file)
    file.close()

    while True:
        for i in range(len(NodeList)):
            NodeList[i].updateStats()

        for i in range(len(NodeList)):
            stats[NodeList[i].name] = NodeList[i].stats


@Server.route('/stats/')
def read_statiscs():

    return render_template('statistic.html')

@Server.route('/get_stats/')
def get_stats():
    if request.method == "GET":
        path = os.getcwd() + '/stats.json'
        data = get_statistics(path)
    else:
        data = "Error!!! You can use only GET request."

    return data
        


def serverRun():
    Server.run(host=ip, port=port)


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=serverRun)
    pullStats_process = multiprocessing.Process(target=pullStats)
    server_process.start()
    pullStats_process.start()
    server_process.join()
    pullStats_process.join()
