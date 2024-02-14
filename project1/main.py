# Each node is a user
class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []

# This class represents a network
class Graph:
    def __init__(self):
        # all members of the network as objects (nodes)
        self.members = []

    def __str__(self):
        # Returns all members of the network
        result = [str(x) for x in self.members]
        return '\n'.join(result)

    # Create new node (user) and append it to the members
    def add_member(self, name, age, location):
        member = Node(name, age, location)
        self.members.append(member)
        return True

    def find_friends(self, name):
        for member in self.members:
            if member.name == name:
                return member.friends
        return None
      
    def shortest_path(graph, friend1, friend2):
        if friend1 not in graph or friend2 not in graph:
            return None  # Handle invalid friend1 or friend2 node

        visited = set()
        queue = [(friend1, [friend1])]

        while queue:
            current_node, path = queue.pop(0)

            if current_node == friend2:
                return path  # Found the shortest path

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None  # No path found

