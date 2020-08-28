#https://www.acmicpc.net/problem/1981

import sys
from collections import deque

sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = 2147383647
l = 0
r = 200

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(mn,mx):

    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if mn <= a[x][y] <= mx:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

    return visited[n-1][n-1] and mn <= a[n-1][n-1] <= mx

def go(diff):
    i = 0
    while i + diff <= 200:
        if bfs(i,i+diff):
            return True
        i+=1
    return False

while l <= r:
    mid = (l+r) // 2
    if go(mid):
        r = mid - 1
        ans = min(ans,mid)
    else:
        l = mid + 1

print(ans)