import random, sys, breadth

all_nodes = []   ## Create data strucutre 20*10 of x,y coordinates.
for x in range(20):
    for y in range(10):
        all_nodes.append([x, y])

example_graph = breadth.SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

breadth.breadth_first_search_1(example_graph, 'A')
