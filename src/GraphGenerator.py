from src import *
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.DiNode import DiNode
import random


class GraphGenerator:

    def __init__(self, vertices, edges):
        self.graph = DiGraph()
        self.v = vertices
        self.e = edges
        self.mc = 0
        self.Generate()

    def Generate(self):
        for vertex in range(self.v):
            self.graph.add_node(vertex, (random.uniform(0, 100), random.uniform(0, 100), 0))

        while self.graph.e != self.e:
            random_pair = (random.randrange(self.v), random.randrange(self.v), random.uniform(0, 40))
            source = random_pair[0]
            destination = random_pair[1]
            weight = random_pair[2]
            self.graph.add_edge(source,destination,weight)
