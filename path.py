from room import Room
from world import World
from player import Player
from collections import defaultdict
import random
import math

class Path: 
    def __init__(self): 
        self.graph = {}
    
    def wander(self, starting_room, move_log):
        # Initialize stack
        stack=[]
        current = starting_room
        stack.append([(current, "")])

        # IN PROGRESS: Keep track of directions
        reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

        while len(stack) > 0: 
            advpath = stack.pop()

            """if len(advpath) > 1:
                for step in advpath[1:]:
                    move_log.append(reverse_direction[step[1]])"""

            popped = advpath[-1]
            vertex = popped[0]
            print(vertex)
            if vertex.id not in self.graph:
                self.graph[vertex.id] = {} # Establish dict entry for this room.

                for next_dir in vertex.get_exits(): # Get all exits

                    self.graph[vertex.id][next_dir] = '?' # Initialize key(s) in graph for this exit

                    next_vert = vertex.get_room_in_direction(next_dir) # Get exit room number
                    
                    if next_vert not in self.graph: # If room hasn't been explored
                        self.graph[vertex.id][next_dir] = next_vert.id # Set exit room ID in graph

                        new_path = list(advpath) # Make a copy of path rather than reference
                        
                        new_path.append((next_vert, next_dir)) # Append this new vert and provide what direction it was
                        move_log.append(next_dir)
                        stack.append(new_path) # Add new room to stack

        sorted_dict = dict(sorted(self.graph.items())) 
        print(sorted_dict)
