#https://www.acmicpc.net/problem/16924

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
c = [[False] * m for _ in range(n)]

answer = []

def check(i,j):
    global answer
    up = 0
    down = 0
    left = 0
    right = 0

    x = i - 1
    y = j

    while x >= 0 and a[x][y] == '*':
        up += 1
        x -= 1

    x = i + 1

    while x < n and a[x][y] == '*':
        down += 1
        x += 1

    x = i
    y = j - 1

    while y >= 0 and a[x][y] == '*':
        left += 1
        y -= 1

    y = j + 1

    while y < m and a[x][y] == '*':
        right += 1
        y += 1

    minimum = min(up,down,left,right)

    while minimum != 0:
        answer.append((i+1,j+1,minimum))
        c[i][j] = True
        if i+minimum < n:
            c[i+minimum][j] = True
        if i-minimum >= 0:
            c[i-minimum][j] = True
        if j + minimum < m:
            c[i][j+minimum] = True
        if j - minimum >= 0:
            c[i][j-minimum] = True
        minimum -= 1

for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            check(i,j)

for i in range(n):
    for j in range(m):
        if a[i][j] == '*' and c[i][j] == False:
            print(-1)
            exit()
print(len(answer))
for ans in answer:
    print(*ans)