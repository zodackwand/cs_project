class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []

class Graph:
    def __init__(self):
        self.members = {}

    def find_friends(self, name):
        if name in self.members:
            return self.members[name].friends
        else:
            return []