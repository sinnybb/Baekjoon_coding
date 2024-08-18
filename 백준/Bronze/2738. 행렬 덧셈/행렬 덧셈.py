n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result = [a[i][j] + b[i][j] for j in range(m)]
    print(' '.join(map(str, result)))