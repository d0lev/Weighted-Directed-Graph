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
        expectd = [3, 6]
        self.assertEqual(actual, expectd)



    # def test_all_out_edges_of_node(self):
    #     self.fail()
    #
    # def test_remove_edge(self):
    #     self.fail()
    #
    # def test_remove_node(self):
    #     self.fail()
    #
    # def test_graph_transpose(self):
    #     self.fail()
    #
    # def test_v_size(self):
    #     self.fail()
    #
    # def test_e_size(self):
    #     self.fail()
    #
    # def test_get_mc(self):
    #     self.fail()
    #
    # def test_get_all_v(self):
    #     self.fail()
    #
    # def test_reset(self):
    #     self.fail()
