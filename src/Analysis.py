import random
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import json
import networkx as nx
import time

class Analysis:
    """simple class that analysis the comparison between python and networkX on a different graphs"""
    def __init__(self):
        self.g = DiGraph()
        self.graph = GraphAlgo(self.g)

    def getGraph(self):
        return self.graph.graph

    def NetworkX(self, tup=None, str=None):
        print(f"This is a test for :{str} \n")
        print("NetworkX :\n")
        print("load method \n")
        try:
            start_time = time.time()
            with open(str, 'r') as my_file:
                json_str = my_file.read()
                graph_from_json = json.loads(json_str)
                graphnx = nx.DiGraph()
                for vertex in graph_from_json['Nodes']:
                    pos = vertex.get('pos')
                    if pos is not None:
                        pos = tuple(map(float, vertex['pos'].split(',')))
                    key = vertex['id']
                    graphnx.add_node(key,pos=pos)

                for edge in graph_from_json['Edges']:
                    source = int(edge['src'])
                    destination = int(edge['dest'])
                    weight = float(edge['w'])
                    graphnx.add_edge(source, destination, weight=weight)

            time_execution = time.time() - start_time
            print("The time execution is : %s\n" % time_execution)
        except IOError as e:
            print(e)

        print("shortest path :\n")
        nx.shortest_path_length(graphnx, source=tup[0].key, target=tup[1].key, method="dijkstra")
        start_time = time.time()
        nx.shortest_path(graphnx, source=tup[0].key, target=tup[1].key, method="dijkstra", weight="weight")
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        print("connected components :\n")
        start_time = time.time()
        list(nx.strongly_connected_components(graphnx))
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        print("=============(END OF TEST)=================")

    def Python(self, str=None):
        print(f"This is a test for :{str} \n")
        print("Python")
        print("load method:\n")
        start_time = time.time()
        self.graph.load_from_json(str)
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        print("shortest path :\n")
        start_time = time.time()
        rand = self.getGraph().v_size()
        source = self.getGraph().get_node(int(random.uniform(0, rand)))
        destination = self.getGraph().get_node(int(random.uniform(0, rand)))
        self.graph.shortest_path(source.getKey(), destination.getKey())
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        print("connected component :\n")
        start_time = time.time()
        self.graph.connected_component(source.key)
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        print("connected components :\n")
        start_time = time.time()
        self.graph.connected_components()
        time_execution = time.time() - start_time
        print("The time execution is : %s\n" % time_execution)
        self.NetworkX((source, destination), str)

    def plotting(self,str):
        self.graph.load_from_json(str)
        self.graph.plot_graph()

if __name__ == '__main__':
    G = Analysis()
    str_1 = "../data/G_10_80_1.json"
    str_2 = "../data/G_100_800_1.json"
    str_3 = "../data/G_1000_8000_1.json"
    str_4 = "../data/G_10000_80000_1.json"
    str_5 = "../data/G_20000_160000_1.json"
    str_6 = "../data/G_30000_240000_1.json"
    list_strs = [str_1,str_2,str_3,str_4,str_5,str_6]
    for test in list_strs:
        G.Python(test)
