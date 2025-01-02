import sys
from collections import deque
queue = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    # push X
    if command[0] == 'push':
        queue.append(int(command[1]))
    
    # pop
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    # size
    elif command[0] == 'size':
        print(len(queue))

    # empty
    elif command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    # front
    elif command[0] == 'front':
        if queue:
            print(queue[0]) 
        else:
            print(-1)

    # back
    elif command[0] == 'back':
        if queue:
            print(queue[-1]) 
        else:
            print(-1)
