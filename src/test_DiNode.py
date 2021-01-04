from unittest import TestCase
from src.DiNode import DiNode


class TestDiNode(TestCase):

    def setUp(self) -> None:
        self.vertices = []
        for x in range(35):
            self.vertices.append(DiNode(x))

    def test_get_key(self):
        expected = 34
        actual = self.vertices[34].getKey()
        self.assertEqual(actual , expected)

    def test_get_info(self):
        node = self.vertices[13]
        actual = node.getInfo()
        expected = "unvisited"
        self.assertEqual(actual, expected)

    def test_set_info(self):
        node = self.vertices[11]
        node.setInfo("visited")
        actual = node.getInfo()
        expected = "visited"
        self.assertEqual(actual, expected)

    def test_get_weight(self):
        node = self.vertices[16]
        node.setWeight(0.314)
        actual = node.getWeight()
        expected = 0.314
        self.assertEqual(actual, expected)


    def test_set_weight(self):
        node = self.vertices[15]
        node.setWeight(35)
        expected = 35
        actual = node.getWeight()
        self.assertEqual(actual, expected)

    def test_set_position(self):
        node = self.vertices[3]
        actual = node.getPosition()
        expected = None
        self.assertEqual(actual,expected)

    def test_get_position(self):
        node = self.vertices[5]
        node.setPosition(1, 2, 3)
        expected = (1,2,3)
        actual = node.getPosition()
        self.assertEqual(actual, expected)
