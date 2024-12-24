from collections import deque

a = int(input())
num = deque(list(range(1, a+1)))

while len(num) != 1 :
    # 첫 숫자 제거
    num.popleft()
    # 그 다음 숫자 맨 뒤로 이동
    f = num.popleft()
    num.append(f)

print(num[0])