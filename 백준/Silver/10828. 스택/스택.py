import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    command = sys.stdin.readline().split()
    
    # push
    if command[0] == 'push':
        stack.append(int(command[1]))
    
    # pop
    elif command[0] == 'pop':
        print(-1) if len(stack) == 0 else print(stack.pop())

    # size
    elif command[0] == 'size':
        print(len(stack))

    # empty
    elif command[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    
    # top
    elif command[0] == 'top':
        print(-1) if len(stack) == 0 else print(stack[-1])