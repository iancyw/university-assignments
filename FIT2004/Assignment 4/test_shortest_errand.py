import unittest
from assignment4 import Graph


class TestShortestErrand(unittest.TestCase):
    def _verify_all_start_dist_pred(self, g, start_dist_pred):
        for start, (dist, pred) in enumerate(start_dist_pred):
            with self.subTest(start=start):
                self.assertEqual(g.dijkstra(start), (dist, pred))

    def test_given(self):
        g = Graph('given_graph3')
        home = 0
        destination = 8
        ice_locs = [1, 5, 8]
        ice_cream_locs = [4, 6]

        length = 6
        path = [0, 1, 0, 3, 6, 7, 8]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_via_dest(self):
        g = Graph('given_graph3')
        home = 0
        destination = 8
        ice_locs = [8]
        ice_cream_locs = [5]

        length = 10
        path = [0, 3, 6, 7, 8, 7, 4, 5, 4, 7, 8]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_single_vertex(self):
        g = Graph('single_vertex')
        home = 0
        destination = 0
        ice_locs = [0]
        ice_cream_locs = [0]

        length = 0
        path = [0]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_pair_dest_all(self):
        g = Graph('pair_graph')
        home = 0
        destination = 1
        ice_locs = [1]
        ice_cream_locs = [1]

        length = 42
        path = [0, 1]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_pair_home_all(self):
        g = Graph('pair_graph')
        home = 0
        destination = 1
        ice_locs = [0]
        ice_cream_locs = [0]

        length = 42
        path = [0, 1]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_fancy(self):
        # just another graph which I provided which actually has
        # "interesting" edge weights
        g = Graph('fancy_graph')
        home = 1
        destination = 3
        ice_locs = [4]
        ice_cream_locs = [0, 6]

        length = 91
        path = [1, 0, 2, 5, 4, 5, 2, 0, 1, 3]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))

    def test_fancy2(self):
        g = Graph('fancy_graph')
        home = 3
        destination = 6
        ice_locs = [5, 4]
        ice_cream_locs = [3, 4]

        length = 56
        path = [3, 1, 0, 2, 5, 4, 6]

        self.assertEqual(g.shortest_errand(home, destination, ice_locs,
                                           ice_cream_locs), (length, path))


if __name__ == '__main__':
    unittest.main()
