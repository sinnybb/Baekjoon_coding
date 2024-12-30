import sys
n = int(sys.stdin.readline())

for _ in range(n):
    vps = str(sys.stdin.readline().strip())
    stack = []
    result = True

    while result:
        if vps[0] == '(':
            stack.append(vps[0])
        else:
            if not stack:
                result = False
                break
            stack.pop()

        vps = vps[1:]
        
        if not vps:
            if stack:
                result = False
            break

    if result:
        print('YES')
    else:
        print('NO')