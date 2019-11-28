import modules.NodeWrapper as nw
import modules.LoadAnalyzer as la
import flask
import queue
import multiprocessing
import threading
import time
import sched

Server = flask.Flask(__name__)
ip = "localhost"
port = "8888"

node_number = 1  # temporary
NodeList = []

MessageQueue = queue.Queue(maxsize=100)

# TODO Написати нормальний механізм додавання нових нод
for i in range(node_number):
    name = "temp"
    ip = "localhost"
    port = "8888"
    NodeList.append(nw.NodeWrapper(name, ip, port))


@Server.route('/send_message/')
def init():
    message = flask.request.json
    MessageQueue.put(message)


# @Server.route('/sender/')
# def sender():
#     if len(NodeList) > 0 and MessageQueue.qsize() > 0:
#         node_index = la.LoadAnalyzer(NodeList)
#         NodeList[node_index].sendMessage(MessageQueue.get())
#     # time.sleep(3)
#     # s.enter(1, 1, sendMessage)
#     # s.run()

# //////////////
# TODO Цей код повинен періодично виконуватись
s = sched.scheduler(time.time, time.sleep)


def sendMessage():
    while True:
        if len(NodeList) > 0 and MessageQueue.qsize() > 0:
            node_index = la.LoadAnalyzer(NodeList)
            NodeList[node_index].sendMessage(MessageQueue.get())


# ticker = threading.Event()
# while not ticker.wait(5):
#     sendMessage()

# //////////////
def serverRun():
    Server.run(host=ip, port=port)


if __name__ == '__main__':
    #Server.run(host=ip, port=port)
    p1 = multiprocessing.Process(target=serverRun)
    p2 = multiprocessing.Process(target=sendMessage)
    p1.start()
    p2.start()
    while True:
        p1.join()
        p2.join()

