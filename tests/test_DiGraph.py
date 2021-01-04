from unittest import TestCase
from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

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

    def test_add_node(self):
        self.assertFalse(self.graph.add_node(0))

    def test_get_node(self):
        self.assertFalse(self.graph.get_node(100))
        self.assertTrue(self.graph.get_node(3))

    def test_add_edge(self):
        self.assertFalse(self.graph.add_edge(1, 4, -9))
        self.assertFalse(self.graph.add_edge(93, 4, -9))
        self.assertTrue(self.graph.add_edge(1, 3, 0.34))
        print(self.graph.edges)

    def test_all_in_edges_of_node(self):
        actual = list(self.graph.all_in_edges_of_node(2).keys())
        expected = [3, 6]
        self.assertEqual(actual, expected)
        self.assertIsNone(self.graph.all_in_edges_of_node(90))

    def test_all_out_edges_of_node(self):
        actual = list(self.graph.all_out_edges_of_node(4))
        expected = [6, 5]
        self.assertEqual(actual, expected)
        self.assertIsNone(self.graph.all_out_edges_of_node(90))
        actual_weight = self.graph.getEdge(4, 6)
        expected = 1.99
        self.assertEqual(actual_weight, expected)

    def test_remove_edge(self):
        tup = (3, 2, self.graph.getEdge(3, 2))
        self.assertFalse(self.graph.remove_edge(0, 31))
        self.assertTrue(self.graph.remove_edge(3, 2))
        actual = self.graph.e_size()
        expected = 8
        self.assertEqual(actual, expected)
        self.assertNotIn(tup, list(self.graph.edges))

    def test_remove_node(self):
        self.assertFalse(self.graph.remove_node(31))
        self.graph.remove_node(3)
        actual = self.graph.v_size()
        expected = 6
        self.assertEqual(actual, expected)
        self.assertNotIn(3, list(self.graph.adjacency))
        self.assertNotIn(3, list(self.graph.vertices))

    def test_graph_transpose(self):
        graph_transpose = self.graph.graph_transpose()
        actual = list(self.graph.edges)
        expected = []
        for source, destination, weight in graph_transpose.edges:
            expected.append((destination, source, weight))

        self.assertListEqual(actual, expected)

    def test_v_size(self):
        actual = self.graph.v_size()
        expected = 7
        self.assertEqual(actual, expected)
        self.graph.remove_node(900)
        self.assertEqual(actual, expected)

    def test_e_size(self):
        actual = self.graph.e_size()
        expected = 9
        self.assertEqual(actual, expected)
        self.graph.remove_edge(0, 900)
        self.assertEqual(actual, expected)

    def test_get_mc(self):
        actual = self.graph.mc
        expected = 16
        self.assertEqual(actual, expected)
        self.graph.remove_node(5)
        actual = self.graph.mc
        expected = 19
        self.assertEqual(actual, expected)

    def test_get_all_v(self):
        actual = list(self.graph.get_all_v())
        expected = [0, 1, 2, 3, 4, 5, 6]
        self.assertListEqual(actual,expected)

    def test_reset(self):
        for vertex in self.graph.vertices.values():
            vertex.setInfo("visited")

        self.graph.Reset()
        actual = 0
        for vertex in self.graph.vertices.values():
            if vertex.getInfo() == "unvisited":
                actual = actual + 1

        expected = 7
        self.assertEqual(actual, expected)