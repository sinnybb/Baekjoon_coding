import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue

    a = [0] * (n + 1)  # Memorization
    a[1], a[2], a[3] = 1, 2, 4  # 초기값 설정
    
    for i in range(4, n + 1):
        a[i] = a[i-1] + a[i-2] + a[i-3]
    
    print(a[n])  
