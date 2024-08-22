n = int(input())
test_list = list(map(int, input().split()))
ma = max(test_list)

new_score = []
for score in test_list :
    new_score.append(score/ma *100) 
test_avg = sum(new_score)/n
print(test_avg)