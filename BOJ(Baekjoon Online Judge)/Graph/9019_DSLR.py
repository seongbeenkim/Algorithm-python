#https://www.acmicpc.net/problem/9019

import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(a,d):
    q = deque()
    q.append(a)
    d[a] = 0

    while q:
        x = q.popleft()
        for i in ['D','S','L','R']:
            nx = x
            if i == 'D':
                nx *= 2
                if nx > 9999:
                    nx %= 10000
            elif i == 'S':
                nx -= 1
                if nx < 0:
                    nx = 9999
            elif i == 'L':
                nx = (nx % 1000) * 10 + (nx // 1000)
            else:
                nx = (nx%10) * 1000 + (nx // 10)

            if d[nx] == -1:
                d[nx] = d[x] + 1
                v[nx] = x
                op[nx] = i
                q.append(nx)

def go(v,op,b):
    if v[b] != -1:
        go(v,op,v[b])
    print(op[b], end = "")
for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    d = [-1] * 10000
    v = [-1] * 10000
    op = [""] * 10000
    bfs(a,d)
    go(v,op,b)
    print()