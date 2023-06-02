from search import AStar


def trivial(node, dest):
    return 0

def manhattan(node, dest):
    return (abs(node.get_x() - dest.get_x()) + abs(node.get_y() - dest.get_y()))

def euclidean(node, dest):
    return ((node.get_x() - dest.get_x())**2 + (node.get_y() - dest.get_y())**2) ** 0.5

def inadmissible(node, dest):
    return 2 * manhattan(node, dest)

def exact_heur(node, dest):
    a_star = AStar(manhattan)
    path = a_star.search(node, dest)
    return len(path) + 1