from collections import Counter
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

counter = Counter(num)
result = [counter[card] for card in cards]

print(*result)