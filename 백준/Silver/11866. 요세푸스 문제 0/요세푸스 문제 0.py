import sys

n, k = map(int, sys.stdin.readline().split())
people = list(range(1,n+1))
result = []

index = 0
while people:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index)) 

print('<', end = "")
print(*result, sep = ', ', end = '>')