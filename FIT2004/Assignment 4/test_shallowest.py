import unittest
from assignment4 import Graph


class TestShallowest(unittest.TestCase):
    def test_given(self):
        g = Graph('given_graph2')
        valid_solutions = [
            (2, 3),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)

    def test_simple_given(self):
        g = Graph('given_graph')
        valid_solutions = [
            (1, 1),
            (2, 1),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)

    def test_grid_given(self):
        g = Graph('given_graph3')
        valid_solutions = [
            (4, 2),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)

    def test_single_vertex(self):
        g = Graph('single_vertex')
        valid_solutions = [
            (0, 0),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)

    def test_pair(self):
        g = Graph('pair_graph')
        valid_solutions = [
            (0, 1),
            (1, 1),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)

    def test_fancy_graph(self):
        g = Graph('fancy_graph')
        valid_solutions = [
            (0, 3),
            (1, 3),
            (2, 3),
            (3, 3),
            (4, 3),
            (5, 3),
            (6, 3),
        ]
        self.assertIn(g.shallowest_spanning_tree(), valid_solutions)


if __name__ == '__main__':
    unittest.main()
