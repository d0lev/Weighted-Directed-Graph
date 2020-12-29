from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.DiNode import DiNode
import json


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


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(1, (3, 2, 1))
    graph.add_node(2, (3, 2, 1))
    graph.add_node(3, (3.324344124234, 2.123345534, 1.124524))
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
    ga.save_to_json('A6.json')
