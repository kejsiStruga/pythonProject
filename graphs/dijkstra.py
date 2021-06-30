from graph_adjacency_list import Graph, Vertex
# graph = {
#     'a': {'b': 10, 'c': 3},
#     'b': {'c': 1, 'd': 2},
#     'c': {'b': 4, 'd': 8, 'e': 2},
#     'd': {'e': 7},
#     'e': {'d': 9}
# }
#
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





































