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
        if vertex in self.vertices:
            self.vertices.pop(vertex)
            return True

    def add_edge(self, vertex1, vertex2):
        # If both exist in the network
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # Add each one to each one!
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
            return True

    def adjacency_matrix(self):
        # I need to add comments
        num_vertices = len(self.vertices)
        matrix = [[0] * num_vertices for _ in range(num_vertices)]  # Initialize the matrix with zeros

        # Fill the matrix based on the connections between vertices
        # r for row c for column
        for r, vertex1 in enumerate(self.vertices):
            for c, vertex2 in enumerate(self.vertices):
                if vertex2 in self.vertices[vertex1]:
                    matrix[r][c] = 1
    #seperate the
        # Prepare row and column labels
        labels = list(self.vertices.keys())
        label_width = max(len(label) for label in labels)  # Calculate width for alignment

        # Generate the formatted matrix with upper layer of IDs
        formatted_matrix = ' ' * (label_width) * 2  # Add space for upper left corner
        for label in labels:
            formatted_matrix += f'{label:>{label_width}} '  # Add column labels
        formatted_matrix += '\n'

        for i, label in enumerate(labels):
            formatted_matrix += f'{label:>{label_width}} '  # Add row label
            formatted_matrix += ' '.join(str(x) for x in matrix[i]) + '\n'  # Add row elements

        return formatted_matrix

    def is_network_connected(network):
        result = True
        #returns true unless case found
        return result

