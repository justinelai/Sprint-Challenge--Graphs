def stack_peek(stack): # errored if i didn't separate into own function
    if len(stack) < 1:
        return None
    else:
        return stack[-1]

def wander(world, starting_room):
    # Initialize stack. 
    # DFS-esque - less popping than attempt one
    graph = {}
    visited = set()
    path = [] # traversal path for return - including backtracking

    stack = [] # current path
    initial = starting_room
    stack.append(initial)

    while len(visited) < len(world): # keep it to maze size since we're optimizing the path

        current = stack_peek(stack) # this time get current WITHOUT popping
        visited.add(current.id) # mark as visited
        graph[current.id] = {} # initialize dict

        discovered = [] # track exits from this room that have been discovered but not visited

        for neighbor_dir in current.get_exits(): # Get any/all exit directions
            graph[current.id][neighbor_dir] = '?' # Initialize key(s) in graph
            neighbor = current.get_room_in_direction(neighbor_dir) # Get exit room info
            graph[current.id][neighbor_dir] = neighbor.id # Add entry
            if neighbor.id not in visited:
                discovered.append((neighbor)) # If it hasn't been visited, queue up - we'll need to visit all BEFORE we pop current

        if len(discovered) > 0: # If there are still rooms to discover, add them to the stack
            next_move = discovered[0]
            stack.append(next_move)
        else: # No more discovered rooms. Pop to backtrack to last current.
            stack.pop()
            next_move = stack_peek(stack)

        for neighbor_dir in current.get_exits(): 
            # instead of trying to parse the move from the stack, break this out and simply mirror the process. get specific direction
            neighbor = current.get_room_in_direction(neighbor_dir)
            if neighbor == next_move:
                path.append(neighbor_dir)

    print(graph)
    return path