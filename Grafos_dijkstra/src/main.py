from dijkstra import Dijkstra
from show_graph import show_graph

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [],
    "E": [("D", 4)]
}

show_graph(graph)
d = Dijkstra(graph)
print(d.run("A"))
