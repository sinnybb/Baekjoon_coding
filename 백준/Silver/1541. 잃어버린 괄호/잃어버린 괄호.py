import sys
input = sys.stdin.readline

form = input().split('-')
result = sum(map(int, form[0].split('+')))
for nums in form[1:]:
    result -= sum(map(int, nums.split('+')))

print(result)