"""

2 Ways of implementing graphs:

1. Adjacency List:
    A: Faster and uses less space for Spare graphs
    DA: Slower for dense graphs

2. Adjacency Matrix:
    A: Faster for dense graphs
    A: Simpler for weighted edges
    DA: Uses more space


"""


class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.neighbors = {}


class Graph(object):
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, v_from, v_to, weight):
        if v_from.name in self.vertices and v_to.name in self.vertices:
            for key, value in self.vertices.items():
                if key == v_from.name:
                    v_from.neighbors[v_to.name] = weight
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, ": " + str(self.vertices[key].neighbors))


# graph = {
#     'a': {'b': 10, 'c': 3},
#     'b': {'c': 1, 'd': 2},
#     'c': {'b': 4, 'd': 8, 'e': 2},
#     'd': {'e': 7},
#     'e': {'d': 9}
# }
#

if __name__ == '__main__':
    g = Graph()

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    g.add_vertex(a)
    g.add_vertex(b)
    g.add_vertex(c)
    g.add_vertex(d)
    g.add_vertex(e)

    g.add_edge(a, b, 10)
    g.add_edge(a, c, 3)
    g.add_edge(b, c, 1)
    g.add_edge(b, d, 2)
    g.add_edge(c, b, 4)
    g.add_edge(c, d, 8)
    g.add_edge(c, e, 2)
    g.add_edge(d, e, 7)
    g.add_edge(e, d, 9)

    g.print_graph()
