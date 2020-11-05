#https://www.acmicpc.net/problem/17142

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
MIN = -1
MAX = 50 * 50
virus = []
zero_count = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            virus.append((i,j))
        elif a[i][j] == 0:
            zero_count += 1

if zero_count == 0:
    print(0)
    exit(0)

l = len(virus)

def bfs(active_virus):
    q = deque()
    d = [[-1] * n for _ in range(n)]

    for idx in active_virus:
        x = virus[idx][0]
        y = virus[idx][1]
        q.append((x,y))
        d[x][y] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] != 1:
                if d[nx][ny] == -1 or d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))

    return check(d)

def check(d):
    maximum = MIN
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                if d[i][j] == -1:
                    return MIN
                else:
                    maximum = max(maximum,d[i][j])

    return maximum



result = []

for i in range(1<<l):
    active_virus = []
    for j in range(l):
        if i & (1<<j):
            active_virus.append(j)

    if len(active_virus) != m:
        continue
    result.append(bfs(active_virus))

result.sort()
answer = MAX

if result[0] == -1 and result[-1] == -1:
    answer = MIN

else:
    for time in result:
        if time == -1:
            continue
        else:
            answer = time
            break
print(answer)