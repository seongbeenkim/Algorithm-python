#https://www.acmicpc.net/problem/13549

import sys
from collections import deque

MAX = 200000
n, k = map(int,sys.stdin.readline().split())
dist = [-1] * (MAX+1)

def bfs(i):
    q = deque()
    next_queue = deque()
    q.append(i)
    dist[i] = 0
    while q:
        x = q.popleft()

        if 2*x <= MAX and dist[2*x] == -1:
            q.append(2*x)
            dist[2*x] = dist[x]

        if x-1 >= 0 and dist[x-1] == -1:
            next_queue.append(x-1)
            dist[x-1] = dist[x] + 1

        if x+1 <= MAX and dist[x+1] == -1:
            next_queue.append(x+1)
            dist[x+1] = dist[x] + 1

        if not q:
            q = next_queue
            next_queue = deque()

bfs(n)
print(dist[k])
