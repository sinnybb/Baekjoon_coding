# A＠B = (A+B)×(A-B)
def fn(a,b):
    return (a+b)*(a-b)

a, b = map(int, input().split())
print(fn(a,b))