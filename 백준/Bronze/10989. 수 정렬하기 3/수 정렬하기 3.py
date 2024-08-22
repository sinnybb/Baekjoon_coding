import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

sorted_list = [0]*10001

for i in range(n):
    sorted_list[int(input())] += 1

for i in range(1, 10001):
    for j in range(sorted_list[i]):
        print(str(i) + "\n")