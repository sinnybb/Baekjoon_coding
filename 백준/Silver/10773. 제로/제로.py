import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    order = int(sys.stdin.readline())
    stack.pop() if order == 0 else stack.append(order)

print(sum(stack))