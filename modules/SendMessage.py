import requests
import sched
import time
from threading import Thread, Event

s = sched.scheduler(time.time, time.sleep)

def post():
    requests.post("http://localhost:8888/sender/")


