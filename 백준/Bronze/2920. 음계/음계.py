series = list(map(int, input().split()))

# 기본 상태
ascending = True
descending = True


for i in range(len(series) - 1):
    if series[i] < series[i + 1]:
        descending = False
    elif series[i] > series[i + 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")