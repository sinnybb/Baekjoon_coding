import sys
input = sys.stdin.readline
n = int(input())

sche = []
for _ in range(n):
    s, e = map(int, input().strip().split())
    sche.append((s,e))

sche.sort(key=lambda x : [x[1], x[0]]) # e 우선 정렬

y = sche[0][1]
count = 1

for i in range(1, n):
    x = sche[i][0]
    if x >= y:
        y = sche[i][1]
        count += 1

print(count) 