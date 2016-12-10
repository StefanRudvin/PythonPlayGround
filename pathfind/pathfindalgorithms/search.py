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

DIAGRAM1_WALLS = [(21,0),(22,2),(21,0),(21,1),(21,2),(21,3),(21,5),(21,4)]

g = breadth.SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]

'''
Next move for Dijkstra’s Algorithm is to use the cost of movement for each stage, the queue needs to come from a different order and the search tracks the costs into the queue.

With a function Gridwithweights() we can get the weights from each edge.
A lower number(weight) is made priority into the queue.

To order queues well we use tuples (priority, item) in the function.
'''
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
