from room import Room
from world import World
from player import Player
import random
import math

class Graph: 
    def __init__(self): 
        self.visited = [False] * 500
        self.parent = [-1] * 500
        self.graph = {}
  
    def find_neighbors(self, room):
        room.get_exits - array of existing exits 

        room.get_room_in_direction("n")
        room.get_room_in_direction("e")
        room.get_room_in_direction("s")
        room.get_room_in_direction("w")

        if not already visited
        append direction, neighbor 

        return list of neighbors

    def log_edges(self, rooms=[]):
        this would adjust the entries in the respective 2 dicts


    def wander(self):
        # create bfs queue
        queue = []
        queue.append(starting_room)

        while queue != []: 
            current = queue.pop(0)
            if self.visited[current] is False:
                self.visited[current] is True:
                if 



