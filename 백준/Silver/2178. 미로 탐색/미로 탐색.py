from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
def bfs(x, y):
    q = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        
        # 사방위 움직임
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1 # 거리 누적
                q.append((nx, ny))
            
            if nx == (n-1) and ny == (m-1):
                return visited[nx][ny]
            
print(bfs(0, 0))