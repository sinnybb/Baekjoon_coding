import sys
n = int(sys.stdin.readline())
stack, p = [], []
find = True
i = 1

for num in range(n):
    m = int(sys.stdin.readline())

    # push
    while i <= m:
        stack.append(i)
        p.append('+')
        i += 1

    # pop
    if stack[-1] == m:
        stack.pop()
        p.append('-')
    else:
        find = False
        
if not find:
    print('NO')
else:
    for j in p:
        print(j, sep='\n')