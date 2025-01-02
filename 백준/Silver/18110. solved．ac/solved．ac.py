import sys
n = int(sys.stdin.readline())

round_func = lambda x: int(x) + 1 if x - int(x) >= 0.5 else int(x) 

if n != 0:
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    threshold = round_func(n * 0.15)
    numbers.sort()

    # 원하는 범위로 재할당
    numbers = numbers[threshold:-threshold] if threshold != 0 else numbers
    average = sum(numbers) / len(numbers)
    print(round_func(average))

else:
    print(0)