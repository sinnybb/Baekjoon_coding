n = int(input())
li1 = list(map(int, input().split()))
li1.sort()
m = int(input())
li2 = list(map(int, input().split()))

for i in range(m):
  find = False
  start = 0
  end = len(li1) - 1
  while start <= end :
    midIdx = (start + end) // 2
    target = li2[i]
    if target < li1[midIdx]:
      end = midIdx - 1
    elif target > li1[midIdx]:
      start = midIdx + 1
    elif target == li1[midIdx]:
      find = True
      break
    
  if find:
    print(1)
  else:
    print(0)