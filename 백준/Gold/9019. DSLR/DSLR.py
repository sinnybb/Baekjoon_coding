from collections import deque, defaultdict
import sys

def dsrl(x, y):
    if y == 'D':
        return 2*x % 10000
    if y == 'S':
        return x-1 if x > 0 else 9999
    if y =='L':
        return (x % 1000)*10 + x//1000
    if y == 'R':
        return (x % 10)*1000 + x//10
      
for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().strip().split()) # 1234 3412

    queue = deque() 
    queue.append(n)

    visited = defaultdict(str)
    visited[n] = ''

    while queue:
        node = queue.popleft()
        if node == m:
            break
        for next_node in ['D', 'S', 'L', 'R']:
            result = dsrl(node, next_node)
            if result not in visited:
                queue.append(result)
                visited[result] = visited[node] + next_node

    print(visited[m])