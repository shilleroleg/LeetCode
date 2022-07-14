from collections import deque


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs(graph, start):
    """Depth-First Search — Поиск вглубину"""
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

print(dfs(graph, 'A'))


def iteractive_dfs(graph, start, path=None):
    """iterative depth first search from start"""
    if path is None:
        path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in path:
            path = path + [v]
            q += graph[v]
    return path

print(iteractive_dfs(graph, 'A'))


def bfs(graph, start):
    """Bread-Firsth Search — Поиск вширину"""
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

print(bfs(graph, 'A'))