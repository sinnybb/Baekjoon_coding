from itertools import combinations as cmb

n, max_value = map(int, input().split())
card = list(map(int, input().split())) 

summation = []

for combination in cmb(card, 3):
    current_sum = sum(combination)
    if current_sum <= max_value: 
        summation.append(current_sum)

if summation:
    print(max(summation))
else:
    print(0) 