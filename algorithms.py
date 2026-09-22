from dataclasses import dataclass
from collections import deque

def get_neighbours(node):
    pass

def reconstruct_path(came_from,start,goal):
    pass

    

def bfs_algorithm(grid, start, goal):
    frontier = deque()
    frontier.append(start)
    came_from = {start:None}
    nodes_expanded = 0
    visited = []
    
    while len(frontier) != 0:
        current = frontier.popleft()

        if current == goal:
            break

        for x in get_neighbours(current):
            if x not in visited:
                nodes_expanded += 1
                came_from[x] = current
                visited.append(x)
                frontier.append(x)

    path = reconstruct_path(came_from, start, goal)

    return path, nodes_expanded

    
