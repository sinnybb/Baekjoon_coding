from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

# I 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x, y = i, j

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        
        # 사방면으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append([nx,ny])

                    if graph[nx][ny] == 'P':
                        count += 1
    
    return count if count > 0 else 'TT'

visited = [[False]*m for _ in range(n)]
print(bfs(x,y))