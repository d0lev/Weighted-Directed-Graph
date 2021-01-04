import sys


class DiNode:

    def __init__(self, key):
        """A Default constructor method"""
        self.key = key
        self.position = None
        self.info = "unvisited"
        self.weight = sys.maxsize

    def getKey(self):
        """
        :return: the key of the node
        """
        return self.key

    def getInfo(self):
        """
        :return: the info of the node
        """
        return self.info

    def setInfo(self, info):
        """
        set the info of the node
        """
        self.info = info

    def getWeight(self):
        """
        :return: the weight of the node
        """
        return self.weight

    def setWeight(self, weight):
        """
        set the weight of the node
        """
        self.weight = weight

    def setPosition(self, x, y, z):
        """
        set the position of the node (tuple)
        """
        self.position = (x, y, z)

    def getPosition(self):
        """
        :return: the position of the node (tuple)
        """
        return self.position

    def __repr__(self) -> str:
        return f"{self.key}"
