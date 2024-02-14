# Each node is a computer
class Node:
    def __init__(self, id):
        self.id = id

# This class represents a network
class Graph:
    def __init__(self):
        # all computers of the network as objects (nodes) in a dict
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            # Create new dict elements with key: vertex and items: set of its connections
            self.vertices[vertex] = set()

    def remove_vertex(self, vertex):
        return None

    def add_edge(self, vertex1, vertex2):
        return None

    def adjacency_matrix(self):
        return None

def is_network_connected(network):
    return None