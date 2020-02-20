#https://www.acmicpc.net/problem/1697

import sys
from collections import deque

MAX = 100001
n, k = map(int,sys.stdin.readline().strip().split())
check = [False] * (MAX+1)
d = [-1] * (MAX+1)

def bfs(start,end):
    q = deque()
    check[start] = True
    q.append(start)
    d[start] = 0

    while q:
        x = q.popleft()
        for next in [x+1,x-1,x*2]:
            if 0 <= next <= MAX and check[next] == False:
                check[next] = True
                q.append(next)
                d[next] = d[x] + 1
bfs(n,k)
print(d[k])