#https://www.acmicpc.net/problem/1939

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
a = [[] for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    a[x].append((y,z))
    a[y].append((x,z))

start, end = map(int,sys.stdin.readline().split())

def bfs(num):
    q = deque()
    q.append(start)
    check = [False for i in range(n+1)]
    check[start] = True

    while q:
        x = q.popleft()
        for to, cost in a[x]:
            if cost >= num and not check[to]:
                q.append(to)
                check[to] = True
    if check[end]:
        return True
    else:
        return False
l = 1
r = 1000000000
ans = 0
while l <= r:
    mid = (l+r) // 2
    if bfs(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)