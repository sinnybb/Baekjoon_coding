import sys
input = sys.stdin.readline

m = int(input().strip())
bitmask = 0

for _ in range(int(m)):
    command = input().strip().split()

    if command[0] == 'add':
        bitmask |= 1 << int(command[1])
    
    elif command[0] == 'remove':
        bitmask &= ~(1 << int(command[1]))

    elif command[0] == 'check':
        print(1 if bitmask & (1 << int(command[1])) else 0)
    
    elif command[0] == 'toggle':
        bitmask ^= (1 << int(command[1])) 

    elif command[0] == 'all':
        bitmask = (1 << 21) - 1

    elif command[0] == 'empty':
        bitmask = 0