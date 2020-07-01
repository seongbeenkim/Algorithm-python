#https://www.acmicpc.net/problem/1525

import sys
from collections import deque

a = [list(map(int,sys.stdin.readline().split())) for i in range(3)]
n = 3

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = -1

start = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            a[i][j] = 9
        start = start * 10 + a[i][j]


q = deque()
q.append(start)
d = dict()
d[start] = 0

while q:
    now_num = q.popleft()
    now = str(now_num)
    z = now.find('9')
    x = z//3
    y = z%3

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            temp = list(now)
            temp[x*3+y], temp[nx*3+ny] = temp[nx*3+ny], temp[x*3+y]
            next_num = int("".join(temp))
            if next_num not in d:
                d[next_num] = d[now_num] + 1
                q.append(next_num)

if 123456789 in d:
    print(d[123456789])
else:
    print(-1)