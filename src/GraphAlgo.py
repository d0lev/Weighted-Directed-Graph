from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.DiNode import DiNode
import json
from queue import *
import sys
import math


class GraphAlgo(GraphAlgoInterface):
    epsilon = 0.0000001

    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        graph_json = {"Nodes": [], "Edges": []}
        with open(file_name, mode='w') as my_file:
            for vertex in self.graph.get_all_v():
                v = self.graph.get_node(vertex)
                pos = str(v.getPosition()[0]) + "," + str(v.getPosition()[1]) + "," + str(v.getPosition()[2])
                id = v.getKey()
                vertex_dict = {'pos': pos, "id": id}
                graph_json["Nodes"].append(vertex_dict)

            for edge in self.graph.edges:
                src = edge[0]
                dest = edge[1]
                weight = edge[2]
                edge_dict = {"src": src, "dest": dest, "w": weight}
                graph_json["Edges"].append(edge_dict)

            graph_json_str = json.dumps(graph_json)
            my_file.write(graph_json_str)
            return True

        return False

    def load_from_json(self, file_name: str) -> bool:
        graph_dis = DiGraph()
        with open(file_name, mode='r') as my_file:
            json_str = my_file.read()
            graph_from_json = json.loads(json_str)

        for vertex in graph_from_json['Nodes']:
            pos = vertex.get('pos')
            if pos is not None:
                pos = tuple(map(float, vertex['pos'].split(',')))
            key = vertex['id']
            graph_dis.add_node(key, pos)

        for edge in graph_from_json['Edges']:
            source = int(edge['src'])
            destination = int(edge['dest'])
            weight = float(edge['w'])
            graph_dis.add_edge(source, destination, weight)

        self.graph = graph_dis
        if self.graph is not None:
            return True
        return False

    def shortest_path(self, source: int, destination: int) -> (float, list):
        tuple_ans = self.dijkstra(source, destination)
        return tuple_ans

    def dijkstra(self, source: int, destination: int) -> (float, list):
        if (source in self.graph.vertices and destination in self.graph.vertices
                and source != destination):
            self.get_graph().Reset()
            pqueue = PriorityQueue()
            src = self.graph.get_node(source)
            src.setWeight(0)
            pqueue.put((0, src))
            while not pqueue.empty():
                vertx = pqueue.get()[1]
                vertx.setInfo("visited")
                for key, weight in self.graph.all_out_edges_of_node(vertx.key).items():
                    neighbour = self.graph.get_node(key)
                    if neighbour.getInfo() == "unvisited":
                        temp_weight = vertx.weight + weight
                        if temp_weight < neighbour.weight:
                            pqueue.put((temp_weight, neighbour))
                            neighbour.setWeight(temp_weight)

            squeue = Queue()
            path = []
            current = self.graph.get_node(destination)
            if current.getWeight() == sys.maxsize:
                return None
            else:
                path.append(current)
                while current is not src:
                    for key, weight in self.graph.all_in_edges_of_node(current.key).items():
                        neighbour = self.graph.get_node(key)
                        if current.weight - weight < self.epsilon:
                            path.append(neighbour)
                            squeue.put(neighbour)

                    current = squeue.get()

            dest = self.graph.get_node(destination).getWeight()
            path.reverse()
            ans = (dest, path)
            return ans
        return None

    def dfs(self):
        self.graph.Reset()
        stack = LifoQueue()
        for key in self.graph.vertices:
            vertex = self.graph.get_node(key)
            if vertex.getInfo() == "unvisited":
                self.dfs_inner(vertex, stack)

        components = []
        graph_transpose = self.graph.graph_transpose()
        while not stack.empty():
            vertex = graph_transpose.get_node(stack.get().key)
            if vertex.getInfo() == "unvisited":
                component = []
                components.append(component)
                self.dfs_reverse(vertex, component, graph_transpose)

        return components

    def dfs_reverse(self, vertex, component, graph_t):
        vertex.setInfo("visited")
        component.append(vertex)
        for neighbour, weight in graph_t.all_out_edges_of_node(vertex.key).items():
            v = graph_t.get_node(neighbour)
            if v.getInfo() == "unvisited":
                self.dfs_reverse(v, component, graph_t)

    def dfs_inner(self, vertex, stack):
        vertex.setInfo("visited")
        for neighbour, weight in self.graph.all_out_edges_of_node(vertex.key).items():
            v = self.graph.get_node(neighbour)
            if v.getInfo() == "unvisited":
                self.dfs_inner(v, stack)

        stack.put(vertex)


if __name__ == '__main__':
    g = DiGraph()
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    galgo = GraphAlgo(g)
    print(galgo.shortest_path(0, 3))
