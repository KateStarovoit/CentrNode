import os
import json

def get_statistics(path_to_file):
    if os.path.exists(path=path_to_file): #якщо файл існує
        with open(path_to_file) as stat_file: #відкриваємо для читання
            data = json.load(stat_file) #считуємо данні з файлу
    else:
        data = "Error!!! File not found!"
    return data
#файла не існує
#файл не той/некоректні данні  
