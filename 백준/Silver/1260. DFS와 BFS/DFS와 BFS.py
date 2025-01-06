from collections import defaultdict, deque
import sys

graph = defaultdict(list)

# 양방향 간선의 그래프
node, edge, start_node = map(int, sys.stdin.readline().strip().split())

for _ in range(edge):
    start, end = map(int,sys.stdin.readline().strip().split())
    graph[start].append(end)
    graph[end].append(start)

for key in graph:
    graph[key].sort()

# DFS
def dfs(start_node, graph):
    stack = [start_node]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return ' '.join(map(str, visited))

# BFS
def bfs(start_node, graph):
    queue = deque()
    queue.append(start_node)
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return ' '.join(map(str, visited))

print(dfs(start_node, graph))
print(bfs(start_node, graph))