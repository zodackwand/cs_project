# Each node is a user
class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []

    def __str__(self):
        return self.name

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

