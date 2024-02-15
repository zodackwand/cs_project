# We can avoid creating a separate class (Node) for computers as was in the previous project,
# because we don't have a list of characteristics for each computer - only its ID.

# This class represents a network
class Graph:
    def __init__(self):
        # all computers's IDs in a list
        self.list = []
        # all computers with connections in a dict
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
        # Get the number of vertices
        num_vertices = len(self.vertices)

        # Initialize the matrix with zeros
        matrix = [[0] * num_vertices for _ in range(num_vertices)]

        # Fill the matrix based on the connections between vertices
        for i, vertex1 in enumerate(self.vertices):
            for j, vertex2 in enumerate(self.vertices):
                if vertex2 in self.vertices[vertex1]:
                    matrix[i][j] = 1

        # Prepare row and column labels
        labels = list(self.vertices.keys())
        label_width = max(len(label) for label in labels)

        # Generate the upper layer
        formatted_matrix = (' ' * (label_width) * 2) + ' '.join(f'{label}' for label in labels) + '\n'

        # Generate the matrix rows with row labels and elements
        for i, label in enumerate(labels):
            formatted_matrix += f'{label} ' + ' '.join(str(x) for x in matrix[i]) + '\n'

        return formatted_matrix


def is_network_connected(network):
    return None

network = Graph()

network.add_vertex('A')
network.add_vertex('B')
network.add_vertex('C')
network.add_vertex('D')

network.add_edge('A', 'B')
network.add_edge('B', 'C')

print(network.adjacency_matrix())