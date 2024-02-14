# Each node is a computer
class Node:
    def __init__(self, id):
        self.id = id

# This class represents a network
class Graph:
    def __init__(self):
        # all computers of the network as objects (nodes)
        self.computers = []