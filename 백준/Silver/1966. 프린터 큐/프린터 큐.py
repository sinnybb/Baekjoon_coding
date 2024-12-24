from collections import deque

times = int(input())

for _ in range(times):
    n, m = map(int, input().split()) # 6 0
    numbers = deque([(num, idx) for idx, num in enumerate(map(int, input().split()))]) # (1,0) (1,1) (9,2) (1,3) (1,4) (1,5)
    target_num = numbers[m][0] # 1
    cnt = 0
    stop = False
  
    # 앞에서부터 확인
    while not stop:
      if not numbers:
        break
    
      if numbers[0][0] == max(numbers, key=lambda x: x[0])[0]:
        a = numbers.popleft()
        cnt += 1
        if a == (target_num, m):
            stop = True

      else:
        numbers.append(numbers.popleft())

    print(cnt)