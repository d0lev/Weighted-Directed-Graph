from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for vertex in range(7):
            self.graph.add_node(vertex)
        self.graph.add_edge(0, 3, 3)
        self.graph.add_edge(1, 3, 1)
        self.graph.add_edge(2, 4, 1.99)
        self.graph.add_edge(3, 2, 7)
        self.graph.add_edge(3, 4, 1.2)
        self.graph.add_edge(4, 6, 1.99)
        self.graph.add_edge(4, 5, 1.8)
        self.graph.add_edge(6, 2, 1)
        self.graph.add_edge(6, 5, 9)

        self.algorithms = GraphAlgo(self.graph)

    def test_get_graph(self):
        self.assertTrue(self.graph, self.algorithms.get_graph())

    def test_save_to_json(self):
        self.assertFalse(self.algorithms.save_to_json("../ghah/gaga"))
        self.assertTrue(self.algorithms.save_to_json("../data/test_check.json"))

    def test_load_from_json(self):
        self.assertTrue(self.algorithms.load_from_json("../data/A0"))
        graph_loaded = DiGraph()
        graph_loaded.add_node(0, (35.18753053591606, 32.10378225882353, 0.0))
        graph_loaded.add_node(1, (35.18958953510896, 32.10785303529412, 0.0))
        graph_loaded.add_node(2, (35.19341035835351, 32.10610841680672, 0.0))
        graph_loaded.add_node(3, (35.197528356739305, 32.1053088, 0.0))
        graph_loaded.add_node(4, (35.2016888087167, 32.10601755126051, 0.0))
        graph_loaded.add_node(5, (35.20582803389831, 32.10625380168067, 0.0))
        graph_loaded.add_node(6, (35.20792948668281, 32.10470908739496, 0.0))
        graph_loaded.add_node(7, (35.20746249717514, 32.10254648739496, 0.0))
        graph_loaded.add_node(8, (35.20319591121872, 32.1031462, 0.0))
        graph_loaded.add_node(9, (35.19597880064568, 32.10154696638656, 0.0))
        graph_loaded.add_node(10, (35.18910131880549, 32.103618700840336, 0.0))

        graph_loaded.add_edge(0, 1, 1.4004465106761335)
        graph_loaded.add_edge(0, 10, 1.4620268165085584)
        graph_loaded.add_edge(1, 0, 1.8884659521433524)
        graph_loaded.add_edge(1, 2, 1.7646903245689283)
        graph_loaded.add_edge(2, 1, 1.7155926739282625)
        graph_loaded.add_edge(2, 3, 1.1435447583365383)
        graph_loaded.add_edge(3, 2, 1.0980094622804095)
        graph_loaded.add_edge(3, 4, 1.4301580756736283)
        graph_loaded.add_edge(4, 3, 1.4899867265011255)
        graph_loaded.add_edge(4, 5, 1.9442789961315767)
        graph_loaded.add_edge(5, 4, 1.4622464066335845)
        graph_loaded.add_edge(5, 6, 1.160662656360925)
        graph_loaded.add_edge(6, 5, 1.6677173820549975)
        graph_loaded.add_edge(6, 7, 1.3968360163668776)
        graph_loaded.add_edge(7, 6, 1.0176531013725074)
        graph_loaded.add_edge(7, 8, 1.354895648936991)
        graph_loaded.add_edge(8, 7, 1.6449953452844968)
        graph_loaded.add_edge(8, 9, 1.8526880332753517)
        graph_loaded.add_edge(9, 8, 1.4575484853801393)
        graph_loaded.add_edge(9, 10, 1.022651770039933)
        graph_loaded.add_edge(10, 0, 1.1761238717867548)
        graph_loaded.add_edge(10, 9, 1.0887225789883779)

        self.assertEqual(self.algorithms.get_graph().v_size(), graph_loaded.v_size())
        self.assertEqual(self.algorithms.get_graph().e_size(), graph_loaded.e_size())
        self.assertEqual(self.algorithms.get_graph().get_mc(), graph_loaded.get_mc())
        self.assertListEqual(self.algorithms.get_graph().edges, graph_loaded.edges)
        self.assertEqual(self.algorithms.get_graph().get_all_v().keys(), graph_loaded.get_all_v().keys())



    # def test_shortest_path(self):
    #     self.fail()
    #
    # def test_dijkstra(self):
    #     self.fail()
    #
    # def test_connected_component(self):
    #     self.fail()
    #
    # def test_connected_components(self):
    #     self.fail()
    #
    # def test_dfs(self):
    #     self.fail()
    #
    # def test_dfs_reverse(self):
    #     self.fail()
    #
    # def test_dfs_inner(self):
    #     self.fail()
    #
    # def test_plot_graph(self):
    #     self.fail()
