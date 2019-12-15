import os
import json

def get_statistics(path_to_file):
    if os.path.exists(path=path_to_file):
        with open(path_to_file) as stat_file:
            data = json.load(stat_file)
    else:
        data = "Error!!! File not found!"
    return data
