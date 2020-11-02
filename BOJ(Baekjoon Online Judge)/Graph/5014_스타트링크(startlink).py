#https://www.acmicpc.net/problem/5014

import sys
from collections import deque

f, s, g, u, d = map(int,sys.stdin.readline().split())

dist = [-1] * (f+1)

q = deque()
q.append(s)
dist[s] = 0

while q:
    x = q.popleft()
    for k in [u,-d]:
        y = x + k
        if 1 <= y <= f:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
            elif dist[y] > dist[x] + 1:
                dist[y] = dist[x] + 1
                q.append(y)
if dist[g] == -1:
    print("use the stairs")
else:
    print(dist[g])