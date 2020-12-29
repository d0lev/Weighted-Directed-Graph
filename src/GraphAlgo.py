from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.DiNode import DiNode
import json
from queue import *


class GraphAlgo(GraphAlgoInterface):

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
        if (source in self.graph.vertices and destination in self.graph.vertices
                and source != destination):
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
        current = graph.get_node(destination)
        path.append(current)
        while current is not src:
            for key, weight in self.graph.all_in_edges_of_node(current.key).items():
                neighbour = self.graph.get_node(key)
                if current.weight - weight == neighbour.weight:
                    path.append(neighbour)
                    squeue.put(neighbour)

            current = squeue.get()
        dest = graph.get_node(destination).getWeight()
        path.reverse()
        ans = (dest, path)
        return ans

if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_edge(1, 4, 1.25)
    graph.add_edge(1, 2, 1.2)
    graph.add_edge(2, 1, 4.14)
    graph.add_edge(2, 3, 3.8)
    graph.add_edge(4, 3, 1.25)
    graph.add_edge(4, 5, 36.1)
    graph.add_edge(3, 5, 1.25)
    ga = GraphAlgo(graph)
