# OOXXOOXXOO / 9
# OXOXOXOXOXOXOX / 7
# OOOOOOOOOO / 55

n = int(input())

for _ in range(n):
    series = input()
    count = 0
    t = 0
    
    for i in range(len(series)):
        if series[i] == "O":
            t += 1
            count += t
        else :
            t = 0

    print(count)