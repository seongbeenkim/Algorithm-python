#https://www.acmicpc.net/problem/2447

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
map = [[' '] * n for _ in range(n)]

def go(x, y, ex, ey, now):

    if now == 1:
        map[x-1][y-1] = "*"
        return

    cnt = now // 3

    go(x, y, x+cnt-1, y+cnt-1, cnt)
    go(x, y+cnt, x+cnt-1, y+cnt+cnt-1, cnt)
    go(x, y+cnt+cnt, x+cnt-1, ey, cnt)

    go(x+cnt, y, x+cnt+cnt-1, y+cnt-1, cnt)
    #go(x+cnt, y+cnt, x+cnt+cnt-1, y+cnt+cnt-1, cnt)
    go(x+cnt, y+cnt+cnt, x+cnt+cnt-1, ey, cnt)

    go(x+cnt+cnt, y, ex, y+cnt-1, cnt)
    go(x+cnt+cnt, y+cnt, ex, y+cnt+cnt-1, cnt)
    go(x+cnt+cnt, y+cnt+cnt, ex, ey, cnt)

go(1, 1, n, n, n)

for i in range(n):
    print(*map[i], sep = "")