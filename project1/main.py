# Add annotations
# Function descriptions
# Test this

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
      
    def shortest_path(self, friend1, friend2):
        if friend1 not in self.members or friend2 not in self.members:
            return None  # Handle invalid friend1 or friend2

        visited = set()
        queue = [(friend1, 0)]  # Queue to store nodes to be explored, containing the start node and its distance

        while queue:
            current_friend, distance = queue.pop(0) # Remove item in queue -> set the value for current_friend & distance

            if current_friend == friend2: # End friend is reached -> return the shortest distance
                return distance  

            if current_friend not in visited: # Friend not visited -> add to visited set & calculate distance
                visited.add(current_friend)

                for friend in self.relationships[current_friend]:
                    if friend not in visited:
                        queue.append((friend, distance + 1))

        return None  # No path found

    def add_relationship(self, memberN1: str, memberN2: str):
        #Check if the names exist in the list of members
        for member in self.members:
            if member.name == memberN1:
                member1 = member
                break
        else:
            print(f"[memberN1] not found")

        for member in self.members:
            if member.name == memberN2:
                member2 = member
                break
        else:
            print(f"[memberN2] not found")

        #Adding each member to each other's lists to create 'relationship'
        member1.friends.append(member2)
        member2.friends.append(member1)