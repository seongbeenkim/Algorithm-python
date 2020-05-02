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

"""
n,k = map(int,sys.stdin.readline().split())
MAX = max(n,k) * 2

d = [-1] * (MAX+1)

q = deque()
q.append(n)
d[n] = 0

while q:
    x = q.popleft()
    temp = 2*x

    while temp <= MAX and d[temp] == -1 and temp != 0:
        q.append(temp)
        d[temp] = d[x]
        temp *= 2

    for i in [x-1,x+1]:
        if 0 <= i <= MAX:
            if d[i] == -1:
                d[i] = d[x] + 1
                q.append(i)
print(d[k])
"""