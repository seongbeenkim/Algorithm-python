#https://www.acmicpc.net/problem/16926

import sys

n, m, r = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
s = min(n,m)//2
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotating(a,n):

    for k in range(s):
        x = k
        y = k
        dir = 0
        temp = a[x][y]

        while dir < 4:
            nx = x + dx[dir]
            ny = y + dy[dir]
            if k <= nx < n-k and k <= ny < m-k:
                a[x][y] = a[nx][ny]
                x = nx
                y = ny
            else:
                dir += 1
        a[k+1][k] = temp

for i in range(r):
    rotating(a,n)

for i in a:
    print(*i)