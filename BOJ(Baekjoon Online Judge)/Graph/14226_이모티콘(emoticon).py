#https://www.acmicpc.net/problem/14226

import sys
from collections import deque

n = int(sys.stdin.readline())
dist = [[-1] * (n+1) for _ in range(n+1)]

def bfs(s,c):
    q = deque()
    q.append((s,c))
    dist[s][c] = 0
    while q:
        s,c = q.popleft()

        if s <= n and dist[s][s] == -1:
            q.append((s,s))
            dist[s][s] = dist[s][c] + 1

        if s+c <= n and dist[s+c][c] == -1:
            q.append((s+c,c))
            dist[s+c][c] = dist[s][c] + 1

        if 0 <= s-1 and dist[s-1][c] == -1:
            q.append((s-1,c))
            dist[s-1][c] = dist[s][c] + 1

bfs(1,0)
ans = 2000
for i in dist[n][1:]:
    if ans > i:
        ans = i
print(ans)