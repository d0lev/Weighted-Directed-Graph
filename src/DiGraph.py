from src.DiNode import DiNode
from src.GraphInterface import GraphInterface
import sys


class DiGraph(GraphInterface):

    def __init__(self):
        self.vertices = {}
        self.adjacency = {}
        self.edges = []
        self.e = 0
        self.mc = 0
        self.v = 0

    def add_node(self, key: int, pos: tuple = None) -> bool:
        """
        adding a node in the graph
        :param key: a key of a node
        :param pos: a position (x,y,z) to be inserted to the new node
        :return: False if the node is already exits in this graph
        """
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
        """
        :param key: a key of a node
        :return: the node that associated with the initial key
        """
        if key in self.vertices.keys():
            return self.vertices[key]

    def add_edge(self, source, destination, weight):
        """
        adding an edge between two nodes that associated with the initial keys
        :param source: the key of the source node
        :param destination: the key of the destination node
        :param weight: the weight of this edge (must be at least 0)
        :return: False if the weight is negative or if the nodes are not exits
        """
        if source in self.vertices.keys() and destination in self.vertices.keys() and weight >= 0:

            if destination in self.adjacency[source]:
                weight = self.getEdge(source, destination)
                tup = (source, destination, weight)
                self.edges.remove(tup)

            else:
                self.e = self.e + 1

            self.adjacency[source][destination] = weight
            self.edges.append((source, destination, weight))
            self.mc = self.mc + 1

            return True
        else:
            return False

    def getEdge(self, source, destination):
        """
        :param source: the key of the source node
        :param destination: the key of the destination node
        :return: the weight of the edge that associated with the initial keys
        """
        return self.adjacency[source][destination]

    def all_in_edges_of_node(self, key: int) -> dict:
        """
        :param key: a key of the node
        :return: a dictionary that represents all the nodes that pointing of the initial key
        """
        if key in self.vertices:
            in_edges = {}
            for vertex in self.vertices:
                if key in self.adjacency[vertex]:
                    weight = self.adjacency[vertex][key]
                    in_edges[vertex] = weight
            return in_edges

    def all_out_edges_of_node(self, key: int) -> dict:
        """
        :param key: a key of a node
        :return: a dictionary that represents all the nodes that pointed by the initial key
        """
        if key in self.vertices:
            return self.adjacency[key]

    def remove_edge(self, source: int, destination: int) -> bool:
        """
        :param source: the key of the source node
        :param destination: the key of the destination node
        :return: the edge between two nodes in the graph
        """
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
        """
        :param key: a key of a node
        :return: True if the node was deleted
        """
        if key in self.vertices:

            for vertex in list(self.all_in_edges_of_node(key)):
                self.remove_edge(vertex, key)

            for vertex2 in list(self.all_out_edges_of_node(key)):
                self.remove_edge(key, vertex2)

            del self.vertices[key]
            del self.adjacency[key]
            self.mc = self.mc + 1
            self.v = self.v - 1

            return True

        return False

    def graph_transpose(self):
        """
        :return: the directed weighted graph transpose
        """
        graph_t = DiGraph()
        for key in self.vertices:
            graph_t.add_node(key)
        for neighbour in self.edges:
            graph_t.add_edge(neighbour[1], neighbour[0], neighbour[2])
        return graph_t

    def v_size(self) -> int:
        """
        :return: the number of nodes in the graph
        """
        return self.v

    def e_size(self) -> int:
        """
        :return: the number of edges in the graph
        """
        return self.e

    def get_mc(self) -> int:
        """
        :return: the mode count of the graph
        """
        return self.mc

    def get_all_v(self) -> dict:
        """
        :return: a dictionary of the nodes in the graph
        """
        return self.vertices

    def Reset(self):
        for key in self.vertices:
            vertex = self.get_node(key)
            vertex.setInfo("unvisited")
            vertex.setWeight(sys.maxsize)

    def __repr__(self) -> str:

        main_str = f"Graph: |V|={self.v} , |E|={self.e}\n"
        main_str += "{"
        counter = 0
        for vertex in self.vertices.keys():
            counter += 1
            main_str += f"{vertex}: {vertex}: |edges out| "
            main_str += f"{len(self.all_out_edges_of_node(vertex).keys())} "
            main_str += "|edges in| "
            main_str += f"{len(self.all_in_edges_of_node(vertex).keys())} "

            if len(self.vertices.keys()) == counter:
                main_str += "}"
            else:
                main_str += ", "

        return main_str
