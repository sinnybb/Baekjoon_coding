import sys
import statistics as st
from collections import Counter
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 평균
print(round(st.mean(numbers)))

# 중앙값
print(st.median(numbers))
count_list = sorted(Counter(numbers).most_common(), key = lambda x : (-x[1], x[0]))

# 최빈값
if N == 1:
    print(numbers[0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])
    else:
        print(count_list[1][0])

# 범위
print(max(numbers)-min(numbers))