import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문 처리
        
        # 상하좌우 이동
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]  

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1  

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j): 
                result += 1

    print(result)