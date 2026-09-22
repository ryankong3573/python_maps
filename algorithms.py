from dataclasses import dataclass
from collections import deque

def get_neighbours(node,graph):
    return graph.get(node, [])

def reconstruct_path(came_from,start,goal):
    path = [goal]
    current = goal

    while current != start:
        current = came_from[current]
        path.append(current)
        
    path.reverse()
    return path, len(path)

def bfs_algorithm(graph, start, goal):
    frontier = deque()
    frontier.append(start)
    came_from = {start:None}
    nodes_expanded = 0
    visited = []
    
    while len(frontier) != 0:
        current = frontier.popleft()

        if current == goal:
            break

        for x in get_neighbours(graph,current):
            if x not in visited:
                nodes_expanded += 1
                came_from[x] = current
                visited.append(x)
                frontier.append(x)

    path, path_length = reconstruct_path(came_from, start, goal)

    return path, path_length, nodes_expanded

    
