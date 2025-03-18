import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book = {} # 이름:번호
book_list = [0] # 번호:이름
for i in range(n):
    name = input().strip()
    book[name] = i+1
    book_list.append(name)

for _ in range(m):
    quest = input().strip()
    if quest.isdigit():
        print(book_list[int(quest)])
    else:
        print(book[quest])