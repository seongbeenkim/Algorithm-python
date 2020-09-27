#https://www.acmicpc.net/problem/16933
## 질문게시판 반례, 테스트 케이스 다 일치하지만 정답 X....

import sys
from collections import deque

n, m, k = map(int,sys.stdin.readline().split())

a = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
d = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
q.append((0,0,0,0))
d[0][0][0] = 1

while q:
    x, y, night, cnt = q.popleft()
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < n and 0 <= ny < m:

            if (d[nx][ny][1-night] == -1 or d[nx][ny][1-night] > d[x][y][night] + 1) and a[nx][ny] == 0:
                d[nx][ny][1-night] = d[x][y][night] + 1
                q.append((nx,ny,1-night,cnt))

            elif (d[nx][ny][1-night] == -1 or d[nx][ny][1-night] > d[x][y][night] + 1) and a[nx][ny] == 1 and night == 0 and cnt < k:
                d[nx][ny][1-night] = d[x][y][night] + 1
                q.append((nx,ny,1-night,cnt+1))

    if d[x][y][1 - night] == -1 or d[x][y][1-night] > d[x][y][night] + 1:
        d[x][y][1 - night] = d[x][y][night] + 1
        q.append((x, y, 1 - night, cnt))

x = d[n-1][m-1][0]
y = d[n-1][m-1][1]

if x == -1 and y == -1:
    print(-1)
elif x == -1 and y != -1:
    print(y)
elif x != -1 and y == -1:
    print(x)
elif x != -1 and y != -1:
    print(min(x,y))