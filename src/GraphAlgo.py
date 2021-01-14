import random
from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
from queue import *
import sys
import math


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        """
        Init the graph on which this set of algorithms operates on.
        :param g: a directed graph
        """
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the underlying graph of which this class works.
        """
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        """
        A method that performs graph object serialization.
        It serialize it to a JSON file, and save it in the given path.
        :param file_name: The path to the out file
        :return: True if the save was successful, False o.w.
        """
        graph_json = {"Nodes": [], "Edges": []}

        try:
            with open(file_name, mode='w') as my_file:
                for vertex in self.graph.get_all_v():
                    v = self.graph.get_node(vertex)
                    if v.getPosition() is None:
                        id = v.getKey()
                        vertex_dict = {"id": id}
                        graph_json["Nodes"].append(vertex_dict)
                    else:
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

        except IOError:
            return False

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        It deserialize it from a JSON file, by loading it from the given path.
        :param file_name: The path of the file
        :return: True if the loading was successful, False o.w.
        """
        graph_dis = DiGraph()

        try:
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
        except IOError:
            return False

        if self.graph is not None:
            return True

        return False

    def shortest_path(self, source: int, destination: int) -> (float, list):
        """
        :param source: The start node id
        :param destination: The end node id
        :return: a tuple contains the distance (float) between source to destination
                 and a list of the shortest path from node source to node destination using Dijkstra's Algorithm
        """
        tuple_path = self.dijkstra(source, destination)
        if tuple_path is None:
            return 'inf', None
        return tuple_path

    def dijkstra(self, source: int, destination: int) -> (float, list):
        """
        This method implements the Dijkstra algorithm . and also keep on each node the shortest path from the source
        node. These nodes enters a PriorityQueue() and the nodes that poll from the queue will be the nodes with the
        shortest distance priority [ a tuple(weight, node) ] and also they will be marked as "visited" . Variant of
        Queue that retrieves open entries in priority order (lowest first). Entries are typically tuples of the form:
        ( priority number (weight / distance) , data (node) ). it follows that the destination node will keep the
        shortest distance from the source node. dijkstra() is using the 'graph.all_in_edges_of_node()' instead of
        transposing the graph.
        :param source: the source of this path.
        :param destination: the destination of this path.
        :return:a tuple contains the distance (float) between source to destination and a list of the shortest
        path from node source to node destination.
        """
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
                        if math.isclose(current.weight - weight, neighbour.weight, rel_tol=1e-5):
                            path.append(neighbour)
                            squeue.put(neighbour)

                    current = squeue.get()

            dest = self.graph.get_node(destination).getWeight()
            path.reverse()

            return dest, path
        return None

    def connected_component(self, key: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node key is a part of.
        This method is using the 'connected_components()' to get and return the specific SCC.
        :param key: The node id
        :return: The list of nodes in the SCC
        """
        if key in self.graph.vertices.keys():
            list_components = self.kosaraju()
            for component in list_components:
                if key in component:
                    return component

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        This method is using 'kosaraju()' - more details check its docs.
        :return: The list of all SCC
        """
        if len(self.graph.vertices) > 0:
            return self.kosaraju()

    def kosaraju(self):
        """
        This method implements the 'Kosaraju algorithm'.
        The Python interpreter limits the depths of recursion to help you avoid infinite recursions,
        resulting in stack overflows.This limit prevents infinite recursion from causing an overflow of
        the C stack and crashing Python.
        That's why instead of using 'sys.setrecursionlimit' (which isn't permissioned in this task)
        we implemented this method iterative way by using stacks ds to act like a recursion.
        The first DFS 'dfs_inner()' is to find all the vertices u that are reachable from vertex v.
        The second DFS 'dfs_reverse()' is to check the reverse, i.e if all u can reach v.
        The reverse check on the second DFS is made by transposing and getting the graph via 'graph_transpose()'.
        Instead of testing each vertex u ( which are reachable from v) and can reach v back,<br>
        the second DFS on the transpose equivalently tests, if v can reach all u and in the end returning the
        specific strongly component.
        :return: The list of all SCC
        """
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

    def dfs_inner(self, vertex, stack):
        """
        This method is getting each unvisited vertex from kosaraju() first loop of vertices and fill the main 'stack' of
        the components traversal order by using 'stack_like_rec' to act like a recursion (because of the restrictions
        detailed in kosaraju() doc). This method is implementing the DFS algorithm iterative way. This is similar to BFS,
        the only difference is queue is replaced by stack. Created a stack_dfs of nodes and visited array -> insert
        the 'vertex' in the stack_dfs -> -> run a while-loop till the stack_dfs is not empty -> pop the element from
        the stack_dfs -> -> for every neighbour and unvisited node of current node, mark 'visited' the node and
        insert it in the stack_dfs -> -> insert it to stack_like_rec -> in the end pop all stack_like_rec to the main
        'stack' (like a recursion).
        :param vertex: a given node for this component.
        :param stack: the main 'stack' of the components traversal order.
        """
        stack_like_rec = LifoQueue()
        stack_dfs = LifoQueue()
        stack_like_rec.put(vertex)
        stack_dfs.put(vertex)
        while not stack_dfs.empty():
            current = stack_dfs.get()
            current.setInfo("visited")
            for neighbour in self.graph.all_out_edges_of_node(current.key).keys():
                w = self.graph.get_node(neighbour)
                if w.getInfo() == "unvisited":
                    w.setInfo("visited")
                    stack_dfs.put(w)
                    stack_like_rec.put(w)

        while not stack_like_rec.empty():
            stack.put(stack_like_rec.get())

    @staticmethod
    def dfs_reverse(vertex, component, graph_t):
        """
        This method is also using the DFS algorithm (iterative) but this time, it will traverse the transposed graph,
        Every call to this method is given with a new empty component that will be filled with the nodes which from
        the given vertex to its SSC.
        :param vertex: a node (DiNode).
        :param component: a new list to be filled with nodes which from vertex SSC.
        :param graph_t: the transposed graph.
        """
        stack_dfs = LifoQueue()
        stack_dfs.put(vertex)
        vertex.setInfo("visited")
        while not stack_dfs.empty():
            current = stack_dfs.get()
            component.append(current.key)
            for neighbour, weight in graph_t.all_out_edges_of_node(current.key).items():
                v = graph_t.get_node(neighbour)
                if v.getInfo() == "unvisited":
                    v.setInfo("visited")
                    stack_dfs.put(v)

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        This method is using `matplotlib.pyplot` which is a state-based interface to matplotlib.
        It provides a MATLAB-like way of plotting.
        pyplot is mainly intended for interactive plots and simple cases of
        programmatic plot generation.
        """
        plt.grid(color='grey', linestyle=':', linewidth=0.5)
        for edge in self.get_graph().edges:
            source = self.get_graph().get_node(edge[0])
            destination = self.get_graph().get_node(edge[1])

            if source.getPosition() is None:
                source.setPosition(random.uniform(0, 40), random.uniform(0, 40), 0)
            if destination.getPosition() is None:
                destination.setPosition(random.uniform(0, 40), random.uniform(0, 40), 0)

            x_list = [source.getPosition()[0], destination.getPosition()[0]]
            y_list = [source.getPosition()[1], destination.getPosition()[1]]
            plt.plot(x_list, y_list, color="purple")

        for key, vertex in self.get_graph().get_all_v().items():
            plt.annotate(str(key), (vertex.getPosition()[0] - 0.0002, vertex.getPosition()[1] + 0.00013), color='green')
            plt.plot(vertex.getPosition()[0], vertex.getPosition()[1], ".", color='black', markersize=14)

        plt.title("Weighted Directed Graph Visualization")
        plt.xlabel("The x axis")
        plt.ylabel("The y axis")
        plt.show()
