import json


def LoadAnalyzer(NodeList, message):
    IndexOfAvailableNode = 0

    for i in range(NodeList):
        NodeList[i].updateStats()

    for i in range(NodeList):
        if NodeList[IndexOfAvailableNode]["load"] > NodeList[i]["load"]:
            IndexOfAvailableNode = i

    return IndexOfAvailableNode
# TODO Напишіть код)))
