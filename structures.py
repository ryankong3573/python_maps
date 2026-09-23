from collections import defaultdict

def create_graph(edges):
    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dict(graph)
