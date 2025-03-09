import sys
input = sys.stdin.readline

t = int(input())
dp = [(1,0), (0,1)] + [(0,0)] * 40 # 0, 1 미리 배치 

for i in range(2, 41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

for _ in range(t):
    num = int(input())
    print(dp[num][0], dp[num][1])