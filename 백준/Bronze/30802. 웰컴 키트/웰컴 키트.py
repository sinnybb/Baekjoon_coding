n = int(input())
s, m , l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())

# 티셔츠
li = [s, m , l, xl, xxl, xxxl]
ttotal = []
for i in range(6):
  if  li[i] % t !=0 :
    a = li[i] //  t 
    ttotal.append(a+1)
  else :
    a = li[i] //  t 
    ttotal.append(a)
print(sum(ttotal))

# 팬
pset = n // p
prest = n % p
print(pset, prest)