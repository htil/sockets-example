import numpy as np
from ioserver import IOServer
import random
from threading import Thread
import json

socketServer = None

def init():
    print("INITIALIZING")

def main():
    global socketServer
    socketServer  = IOServer()
    socketServer.on("initialize", lambda x: init())
    socketServer.run()

if __name__ == "__main__":
    main()