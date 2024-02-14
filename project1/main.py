class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []


class Graph:
    def __init__(self):
        self.members = {}

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            return True
        else:
            print(f"{member} is already here!")
            return False

    def find_friends(self, name):
        if name in self.members:
            return self.members[name].friends
        else:
            return []
        
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



        
        



