# We can avoid creating a separate class (Node) for computers as was in the previous project,
# because we don't have a list of characteristics for each computer - only its ID.

# This class represents a network
class Graph:
    def __init__(self):
        # all computers of the network as objects (nodes) in a dict
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            # Create new dict elements with key: vertex and items: set of its connections
            self.vertices[vertex] = set()
            return True

    def remove_vertex(self, vertex):
        return None

    def add_edge(self, vertex1, vertex2):
        # If both exist in the network
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # Add each one to each one!
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
            return True

    def adjacency_matrix(self):
        return None

def is_network_connected(network):
    return None