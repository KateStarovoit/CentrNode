import os
import json

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

def get_statistics(path_to_file):
    if os.path.exists(path=path_to_file):
        with open(path_to_file) as stat_file:
            data = json.load(stat_file)
    else:
        data = {'Error!!!' : "File not found."}
    return data
