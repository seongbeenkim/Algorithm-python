#https://www.acmicpc.net/problem/16956

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < m and a[x][y] == '.':
                    a[x][y] = 'D'
        elif a[i][j] == 'W':
            q.append((i,j))
            check[i][j] = True

is_safe = True

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
            if a[nx][ny] == 'S':
                is_safe = False
                break
            elif a[nx][ny] == '.':
                q.append((nx,ny))
                check[nx][ny] = True

    if not is_safe:
        break

if is_safe:
    print(1)
    for d in a:
        print(*d, sep='')
else:
    print(0)