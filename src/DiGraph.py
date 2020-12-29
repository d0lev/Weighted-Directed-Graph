from builtins import *
from src.DiNode import DiNode
from src.GraphInterface import GraphInteface


class DiGraph(GraphInteface):

    def __init__(self):
        self.vertices = {}
        self.adjacency = {}
        self.edges = []
        self.e = 0
        self.mc = 0
        self.v = 0

    def add_node(self, key: int, pos: tuple = None) -> bool:
        if key not in self.vertices:
            node = DiNode(key)
            if pos is not None:
                node.setPosition(pos[0], pos[1], pos[2])
            self.vertices[key] = node
            self.adjacency[key] = {}
            self.v = self.v + 1
            self.mc = self.mc + 1
            return True
        else:
            return False

    def get_node(self, key) -> DiNode:
        if key in self.vertices.keys():
            return self.vertices[key]

    def add_edge(self, source, destination, weight):
        if source in self.vertices.keys() and destination in self.vertices.keys():
            self.adjacency[source][destination] = weight
            self.edges.append((source, destination, weight))
            self.e = self.e + 1
            self.mc = self.mc + 1
            return True
        else:
            return False

    def all_in_edges_of_node(self, key: int) -> dict:
        if key in self.vertices:
            in_edges = {}
            for vertex in self.vertices:
                if key in self.adjacency[vertex]:
                    weight = self.adjacency[vertex][key]
                    in_edges[vertex] = weight
            return in_edges

    def all_out_edges_of_node(self, key: int) -> dict:
        if key in self.vertices:
            return self.adjacency[key]

    def remove_edge(self, source: int, destination: int) -> bool:
        if source in self.vertices.keys() and destination in self.vertices.keys():
            if destination in self.adjacency[source]:
                weight = self.adjacency[source][destination]
                del self.adjacency[source][destination]
                self.edges.remove((source, destination, weight))
                self.mc = self.mc + 1
                self.e = self.e - 1
                return True
        return False

    def remove_node(self, key: int) -> bool:
        if key in self.vertices:

            for vertex in list(self.all_in_edges_of_node(key)):
                self.remove_edge(vertex, key)

            for vertex2 in list(self.all_out_edges_of_node(key)):
                self.remove_edge(key, vertex2)

            del self.vertices[key]
            self.mc = self.mc + 1
            self.v = self.v - 1

            return True

        return False

    def edge_transpose(self) -> list:
        transpose_list = []
        for tup in self.edges:
            n = (tup[1], tup[0], tup[2])
            transpose_list.append(n)
        return transpose_list

    def v_size(self) -> int:
        return self.v

    def e_size(self) -> int:
        return self.e

    def get_mc(self) -> int:
        return self.mc

    def get_all_v(self) -> dict:
        return self.vertices



if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1, (3, 2, 1))
    graph.add_node(2, (3, 2, 1))
    graph.add_node(3, (3, 2, 1))
    graph.add_node(4, (3, 2, 1))
    graph.add_node(5, (3, 2, 1))
    graph.add_node(6, (3, 2, 1))
    graph.add_edge(1, 2, 1.2)
    graph.add_edge(1, 4, 1.3)
    graph.add_edge(2, 3, 1.5)
    graph.add_edge(3, 6, 1.6)
    graph.add_edge(4, 1, 1.9)
    graph.add_edge(4, 5, 1.4)
    graph.add_edge(5, 3, 1.7)
    graph.add_edge(5, 4, 1.4)

