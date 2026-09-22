from dataclasses import dataclass
from collections import deque

def bfs_algorithm(grid, start, end):
    frontier = deque()
    frontier.append(start)
    came_from = {start:None}
    
    current = frontier.popleft()
    
