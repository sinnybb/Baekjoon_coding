import sys
input = sys.stdin.readline

n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]

# 계단이 하나인 경우
if n == 1:
    print(stairs[0])
    exit()

# memorization
dp = [0] * n

# 초기값 설정
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]

# 계단이 두 개일 때 예외 처리
if n == 2:
    print(dp[1])
    exit()

# 세 번째 계단 초기값 설정
dp[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])