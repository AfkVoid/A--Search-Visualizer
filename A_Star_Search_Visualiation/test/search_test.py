import os, sys
import unittest
import tkinter as tk

sys.path.insert(1, '../search visualizer')
from node import *
from search import *
from heuristics import *

class TestNode(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.map = NodeCollection()
        for i in range(20):
            for j in range(20):
                frm = tk.Frame()
                node = Node(frm, i, j, self.map)
                self.map.add(node)
        unittest.TestCase.__init__(self, *args, **kwargs)

    def test_trivial(self):
        walls = set()
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(manhattan)
        path = a_star.search(start, dest)
        self.print_test('test_trivial', start, dest, walls, path)

    def test_wall_simple(self):
        walls = set()
        for x, y in [[3, 1], [3, 2], [3, 3], [3, 4]]:
            node = self.map.get_from_pos(x, y)
            walls.add(node)
            node.wall_on()
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(manhattan)
        path = a_star.search(start, dest)
        self.print_test('test_wall_simple', start, dest, walls, path)

    def test_no_path(self):
        walls = set()
        for x, y in [[0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [3, 0]]:
            node = self.map.get_from_pos(x, y)
            walls.add(node)
            node.wall_on()
        start = self.map.get_from_pos(1, 1)
        dest = self.map.get_from_pos(5, 4)
        a_star = AStar(manhattan)
        path = a_star.search(start, dest)
        self.print_test('test_no_path', start, dest, walls)
        self.assertEqual(len(path), 0)

    def print_test(self, name, start, dest, walls, path=None):
        print()
        print(name)
        print(f"Start: {start}, Destination: {dest}")
        if walls:
            print(f"Walls: { {w for w in walls} }")
        else:
            print('Walls: None')
        if path is not None:
            print(f"path: { [node for node in path] }")
        print()

if __name__ == '__main__':
    unittest.main()