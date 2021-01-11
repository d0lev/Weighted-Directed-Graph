import random
from typing import List

from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.DiNode import DiNode
from src.GraphAlgo import GraphAlgo
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from queue import *
import networkx as nx
import sys
import math
import time


class Analysis:

    def __init__(self):
        self.g = DiGraph()
        self.graph = GraphAlgo(self.g)

    def getGraph(self):
        return self.graph.graph

    def NetworkX(self, tup=None):
        graphnx = nx.DiGraph()
        vertices = list(self.getGraph().vertices.keys())
        graphnx.add_nodes_from(vertices)

        for edge in self.getGraph().edges:
            graphnx.add_edge(edge[0], edge[1], weight=edge[2])

        print("NetworkX :")
        print("==========================================================")
        print("shortest path :\n")
        length = nx.shortest_path_length(graphnx, source=tup[0].key, target=tup[1].key, method="dijkstra")
        start_time = time.time()
        path = nx.shortest_path(graphnx, source=tup[0].key, target=tup[1].key, method="dijkstra", weight="weight")
        time_execution = time.time() - start_time
        print(f"The shortest path between {tup[0].key} and {tup[1].key} is : {length} \n"
              f"And the path is : {path} ")
        print("The time execution is : %s\n" % time_execution)
        print("==========================================================")
        print("connected components :\n")
        start_time = time.time()
        components = list(nx.strongly_connected_components(graphnx))
        time_execution = time.time() - start_time
        print(f"The strongly components of graph is : \n"
              f"{components}\n")
        print("The time execution is : %s\n" % time_execution)

    def Python(self, str=None):
        self.graph.load_from_json(str)
        start_time = time.time()
        rand = len(self.getGraph().vertices)
        source = self.getGraph().get_node(0)
        destination = self.getGraph().get_node(4)
        tuple_ans = self.graph.shortest_path(source.key, destination.key)
        time_execution = time.time() - start_time
        weight = tuple_ans[0]
        path = tuple_ans[1]
        print("shortest path :\n")
        print(f"The shortest path between {source.key} and {destination.key} is : {weight} \n"
              f"And the path is : {path} ")
        print("The time execution is : %s\n" % time_execution)
        print("connected component :\n")
        start_time = time.time()
        component = self.graph.connected_component(source.key)
        time_execution = time.time() - start_time
        print(f"The strongly component of node : {source.key} is : \n"
              f"{component}\n")
        print("The time execution is : %s\n" % time_execution)
        print("connected components :\n")
        start_time = time.time()
        components = self.graph.connected_components()
        time_execution = time.time() - start_time
        print(f"The strongly components of graph is : \n"
              f"{components}\n")
        print("The time execution is : %s\n" % time_execution)
        self.NetworkX((source, destination))


if __name__ == '__main__':
    G = Analysis()
    G.Python("../data/G_30000_240000_1.json")
