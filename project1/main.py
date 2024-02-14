class Node:
    def __init__(self, name, age=None, location=None):
        self.name = name
        self.age = age
        self.location = location
        self.friends = []


class Graph:
    def __init__(self):
        self.members = {}

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            return True
        else:
            print(f"{self.name} is already friends with {friend.name}")
            return False

    def find_friends(self, name):
        if name in self.members:
            return self.members[name].friends
        else:
            return []



