from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import json
import string


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph


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
    ga = GraphAlgo(graph)
    ga.load_from_json('../data/T0.json')
    print(ga.get_graph().get_node(0).getPosition())
