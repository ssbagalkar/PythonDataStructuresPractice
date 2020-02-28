"Task.Implement connected components"
# from collections import dequeue

class Node(object):
    def __init__(self, name):
        self.__name  = name
        self.__edges = set()

    @property
    def name(self):
        return self.__name

    @property
    def edges(self):
        return set(self.__edges)

    def add_edge(self, other):
        self.__edges.add(other)
        other.__edges.add(self)


def connected_components(graph_nodes):
    pass



if __name__ == "__main__":
    # Tree.
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.add_edge(b)    #      a
    #a.add_edge(c)   #     /
    b.add_edge(d)    #    b   c
    c.add_edge(e)    #   /   / \
    c.add_edge(f)    #  d   e   f

    # Single node.
    g = Node("g")

    # Cycle
    h = Node("h")
    i = Node("i")
    j = Node("j")
    k = Node("k")
    h.add_edge(i)    #    h----i
    i.add_edge(j)    #    |    |
    j.add_edge(k)    #    |    |
    k.add_edge(h)    #    k----j

    # Put all the nodes together in one big set.
    nodes = {a, b, c, d, e, f, g, h, i, j, k}

    # Find all the connected components.
    number = 1
    for components in connected_components(nodes):
        names = sorted(node.name for node in components)
        names = ", ".join(names)
        print("Group #{}: {}".format(number, names))
        number += 1


