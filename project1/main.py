class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []

class Graph:
    def __init__(self):
        self.members = {}