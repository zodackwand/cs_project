class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []

    def __str__(self):
        return self.name

class Graph:
    def __init__(self):
        self.members = []

    def __str__(self):
        result = [str(x) for x in self.members]
        return '\n'.join(result)

    def add_member(self, name, age, location):
        if name not in self.members:
            member = Node(name, age, location)
            self.members.append(member)
            return True
        else:
            print(f"{name} is already here!")
            return False

    def find_friends(self, name):
        for member in self.members:
            if member.name == name:
                return member.friends
        return None

