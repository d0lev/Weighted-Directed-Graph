import sys


class DiNode:

    def __init__(self, key):
        """A Default constructor method"""
        self.key = key
        self.position = (0, 0, 0)
        self.info = "unvisited"
        self.weight = sys.maxsize

    def getKey(self):
        return self.key

    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def setPosition(self, x, y, z):
        self.position = (x, y, z)

    def getPosition(self):
        return self.position

    def __str__(self):
        return f"{self.getKey()},{self.getWeight()}"


