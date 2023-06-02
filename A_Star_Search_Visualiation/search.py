import node
import data_structures


class AbstractSearch:
    def search(self, start, dest):
        """Finds and draws the shortest path from start (type Node) to the
        destination, dest (type Node). Returns a path. Should update
        self.searched for use in the GUI."""
        pass

    def get_searched(self):
        """Returns a list of nodes in the order they were inspected in
        the last call of self.search()."""
        pass

class AStar(AbstractSearch):
    def __init__(self, heuristic):
        """The heuristic should be a function that takes in two nodes and
        outputs a number."""
        AbstractSearch.__init__(self)
        self.heuristic = heuristic

    def search(self, start, dest):
        """Performs A* search from start to destination (both Node objects).
        Returns a path, which is a list of Nodes. Updates self.searched."""
        self.searched = []

        closed = set()
        best_parents = {start: None}
        g = {start: 0}

        # Items: (node, parent). Priority: f value
        fringe = data_structures.PriorityQueue()
        fringe.push((start, None), 0 + self.heuristic(start, dest))

        while not fringe.isEmpty():
            # Get node with min f from fringe
            curr, curr_parent = fringe.pop()

            # Destination is reached
            if curr is dest:
                path = []
                while curr is not None:
                    path.append(curr)
                    curr = best_parents[curr]
                # reverse path, exclude start and destination nodes
                return path[len(path)-2:0:-1]

            # Avoid checking nodes repeatedly
            if curr not in closed:
                closed.add(curr)
                best_parents[curr] = curr_parent

                # Plan to color curr in GUI
                if curr is not start:
                    self.searched.append(curr.get_frm())

                # Check each of the current node's successors
                for succ in curr.get_succ():
                    if succ not in closed:
                        best_parents[succ] = curr
                    g[succ] = g[curr] + 1
                    f_val = g[succ] + self.heuristic(succ, dest)
                    fringe.push((succ, curr), f_val)

        return []

    def get_searched(self):
        """Returns a list of tkinter Frames in the order they were inspected in
        the last call of self.search()."""
        return self.searched