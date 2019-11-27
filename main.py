import modules.NodeWrapper as nw
import modules.NodeAnalyzer as na
import flask
import queue

Server = flask.Flask(__name__)
ip = "localhost"
port = "8888"

node_number = 1  # temporary
NodeList = []

MessageQueue = queue.Queue()

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


# //////////////
# TODO Цей код повинен періодично виконуватись
if NodeList and MessageQueue:
    node_index = na.NodeAnalyzer(NodeList)
    NodeList[node_index].sendMessage(MessageQueue.get())
# //////////////

if __name__ == '__main__':
    Server.run(host=ip, port=port)
