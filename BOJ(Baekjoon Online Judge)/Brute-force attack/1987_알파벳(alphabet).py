#https://www.acmicpc.net/problem/1987

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(sys.stdin.readline()) for _ in range(n)]
check = [False] * 26

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def go(i,j,cnt):
    ans = 1

    if ans < cnt:
        ans = cnt

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            alpha = ord(a[nx][ny])-ord('A')
            if not check[alpha]:
                check[alpha] = True
                temp = go(nx,ny,cnt+1)
                ans = max(temp,ans)
                check[alpha] = False
    return ans

check[ord(a[0][0]) - ord('A')] = True
print(go(0,0,1))