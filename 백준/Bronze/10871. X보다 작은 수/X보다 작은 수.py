n, x = map(int, input().split())
nset = list(map(int, input().split()))
result = []

for num in nset:
  if num < x:
    result.append(num)
print(" ".join(map(str,result)))