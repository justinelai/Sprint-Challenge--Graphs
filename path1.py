from room import Room

class Path: 
    def __init__(self): 
        self.graph = {}

    def wander(self, starting_room, move_log):
        # Initialize stack
        stack=[]
        current = starting_room
        stack.append([(current, "")])
        # IN PROGRESS: Need to keep track of directions for when it backtracks?
        reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
        while len(stack) > 0: 
            advpath = stack.pop()
            popped = advpath[-1]
            vertex = popped[0]
            if popped[1]:
                move_log.append(reverse_direction[popped[1]])
            if vertex.id not in self.graph: # If there's no entry in my graph
                self.graph[vertex.id] = {} # Establish dict entry for this room.
                for next_dir in vertex.get_exits(): # Get all exits
                    self.graph[vertex.id][next_dir] = '?' # Initialize key(s) in graph for this exit
                    next_vert = vertex.get_room_in_direction(next_dir) # Get exit room number
                    move_log.append(next_dir)
                    if next_vert not in self.graph: # If room hasn't been explored
                        self.graph[vertex.id][next_dir] = next_vert.id # Set exit room ID in graph
                        new_path = list(advpath) # Make a copy of path rather than reference
                        new_path.append((next_vert, next_dir)) # Append this new vert and provide what direction it was
                        move_log.append(next_dir)
                        stack.append(new_path) # Add new room to stack     
        sorted_dict = dict(sorted(self.graph.items())) 
        print(sorted_dict)