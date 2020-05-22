#https://www.acmicpc.net/problem/1987

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline()) for _ in range(n)]
check = [False] * 26
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def go(i,j,cnt):
    global ans
    ans = max(cnt,ans)

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not check[ord(a[nx][ny])-ord('A')]:
            check[ord(a[nx][ny]) - ord('A')] = True
            go(nx,ny,cnt+1)
            check[ord(a[nx][ny]) - ord('A')] = False

check[ord(a[0][0]) - ord('A')] = True
go(0,0,1)
print(ans)