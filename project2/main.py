# We can avoid creating a separate class (Node) for computers as was in the previous project,
# because we don't have a list of characteristics for each computer - only its ID.

# This class represents a network
class Graph:
    def __init__(self):
        # all computers's IDs in a list
        self.list = []
        # all computers with connections in a dict
        self.vertices = {}
        
    def __str__(self):
        return f"{self.vertices}"

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.list.append(vertex)
            # Create new dict elements with key: vertex and items: set of its connections
            self.vertices[vertex] = set()
            return True

    def remove_vertex(self, vertex):
        # Delete vertex from ID list
        self.list.remove(vertex)
        # Delete all connections with vertex
        for id in self.verices:
            if vertex in self.vertices[id]:
                self.vertices[id].remove(vertex)
        
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
    
    def generate_ring_connection(self):
        # Check if there is enough vertices to create a network
        vertice_num = len(self.vertices)
        if vertice_num < 3:
            return None
        
        # Connect each ID vertice to its neighbor to form a ring
        for id in range(vertice_num - 1):
            vertex1 = self.list[id]
            vertex2 = self.list[id + 1]
            self.add_edge(vertex1, vertex2)
            
        # Connect the first and the last ID to complete the ring
        self.add_edge(self.list[0], self.list[-1])
        
        return True
    
    def generate_star_connection(self, central_node = None):
        # Check if the central node is in the network
        if central_node not in self.list:
            return None
        
        for id in self.list:
            # Link every vertice to the central node (excluding itself)
            if id == central_node in self.vertices:
                self.vertices[id] = set(self.list).difference(central_node)
            # Link specific vertice to the central node
            else:
                self.vertices[id] = {central_node}
                
        return True
        


def is_network_connected(network):
    return None

# Sample raw network: A - B - C - D
network = Graph()

network.add_vertex('A')
network.add_vertex('B')
network.add_vertex('C')
network.add_vertex('D')
network.add_edge('A', 'B')
network.add_edge('B', 'C')
network.add_edge('C', 'D')

# Modified by the ring method, each node has two neighbour connections and forms a ring
network.generate_ring_connection()
print(f"\nSample ring connection: {network}")

# Modified by the star method, each node is linked to a central node specified by a user
network.generate_star_connection('A')
print(f"\nSample star connection: {network}")





