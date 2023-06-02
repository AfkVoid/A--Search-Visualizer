import sys
import unittest
import tkinter as tk

sys.path.insert(1, '../search visualizer')
from node import *

class TestNode(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.map = NodeCollection()
        for i in range(20):
            for j in range(20):
                frm = tk.Frame()
                node = Node(frm, i, j, self.map)
                self.map.add(node)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_succ_simple(self):
        node = self.map.get_from_pos(5, 5)
        successors = node.get_succ()
        self.assertEqual(len(successors), 4)

        self.assertEqual(successors[0].get_x(), 5)
        self.assertEqual(successors[1].get_x(), 6)
        self.assertEqual(successors[2].get_x(), 5)
        self.assertEqual(successors[3].get_x(), 4)

        self.assertEqual(successors[0].get_y(), 6)
        self.assertEqual(successors[1].get_y(), 5)
        self.assertEqual(successors[2].get_y(), 4)
        self.assertEqual(successors[3].get_y(), 5)

    def test_succ_corner(self):
        node = self.map.get_from_pos(0, 0)
        successors = node.get_succ()
        self.assertEqual(len(successors), 2)

        self.assertEqual(successors[0].get_x(), 0)
        self.assertEqual(successors[1].get_x(), 1)

        self.assertEqual(successors[0].get_y(), 1)
        self.assertEqual(successors[1].get_y(), 0)

if __name__ == '__main__':
    unittest.main()