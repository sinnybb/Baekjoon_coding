times = int(input())  

for _ in range(times):
    k = int(input())  # 층 수
    n = int(input())  # 호 수

    people = [i for i in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]  

    print(people[-1]) 