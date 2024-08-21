n, m = map(int, input().split())

# 패턴 생성
pattern1 = []
pattern2 = []
for i in range(8):
    p1 = ''.join('W' if (i + j) % 2 == 0 else 'B' for j in range(8))
    p2 = ''.join('B' if (i + j) % 2 == 0 else 'W' for j in range(8))
    pattern1.append(p1)
    pattern2.append(p2)

# 입력 패턴
inputpattern = []
for _ in range(n):
    col = str(input())
    inputpattern.append(col)

# 다시 칠해야 할 정사각형 수 계산
def count_repaints(inputpattern, pattern):
    score = 0
    for i in range(8):
        for j in range(8):
            if inputpattern[i][j] != pattern[i][j]:
                score += 1
    return score

min_repaints = float('inf')

# 모든 8x8 부분을 확인
for i in range(n - 7):
    for j in range(m - 7):
        # 8x8 부분 추출
        sub_pattern = [inputpattern[x][j:j + 8] for x in range(i, i + 8)]
        
        # 패턴 비교
        p1score = count_repaints(sub_pattern, pattern1)
        p2score = count_repaints(sub_pattern, pattern2)
        
        # 최소값 업데이트
        min_repaints = min(min_repaints, p1score, p2score)

print(min_repaints)