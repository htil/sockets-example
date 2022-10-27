#import numpy as np
from ioserver import IOServer
import random
from threading import Thread
import json
import time

socketServer = None


def init():
    global socketServer
    print("INITIALIZING")
    while True:
        time.sleep(0.1)
        socketServer.send('data', random.random() * 30)


def main():
    global socketServer
    socketServer = IOServer()
    socketServer.on("initialize", lambda x: init())
    socketServer.run()


if __name__ == "__main__":
    main()
