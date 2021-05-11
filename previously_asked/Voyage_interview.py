"Task.Implement connected components"

# I was asked the question from the following link:
# https://breakingcode.wordpress.com/2013/04/08/finding-connected-components-in-a-graph/
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


# The function to look for connected components.
def connected_components(nodes):

    # List of connected components found. The order is random.
    result = []

    # Make a copy of the set, so we can modify it.
    nodes = set(nodes)

    # Iterate while we still have nodes to process.
    while nodes:

        # Get a random node and remove it from the global set.
        n = nodes.pop()

        # This set will contain the next group of nodes connected to each other.
        group = {n}

        # Build a queue with this node in it.
        queue = [n]

        # Iterate the queue.
        # When it's empty, we finished visiting a group of connected nodes.
        while queue:
            # Consume the next item from the queue.
            n = queue.pop(0)

            # Fetch the neighbors.
            neighbors = n.edges

            # Remove the neighbors we already visited.
            neighbors.difference_update(group)

            # Remove the remaining nodes from the global set.
            nodes.difference_update(neighbors)

            # Add them to the group of connected nodes.
            group.update(neighbors)

            # Add them to the queue, so we visit them in the next iterations.
            queue.extend(neighbors)

        # Add the group to the list of groups.
        result.append(group)

    # Return the list of groups.
    return result


if __name__ == "__main__":
    # Tree.
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.add_edge(b)    #      a
    a.add_edge(c)    #      /\
    b.add_edge(d)    #     b  c
    c.add_edge(e)    #    /  / \
    c.add_edge(f)    #   d   e  f

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


