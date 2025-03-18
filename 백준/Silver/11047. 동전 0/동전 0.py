import sys
input = sys.stdin.readline
n, k = map(int, input().split())

money = sorted([int(input()) for _ in range(n)], reverse=True)
count = 0

for coin in money:
    if k >= coin:
        count += k // coin
        k %= coin
print(count)