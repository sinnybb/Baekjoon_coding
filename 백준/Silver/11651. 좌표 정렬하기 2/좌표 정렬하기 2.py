n = int(input())
coord = []

for _ in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

coord.sort(key=lambda point: (point[1], point[0]))

for x, y in coord:
    print(x, y)