#https://www.acmicpc.net/problem/2448

import sys
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())
map = [[" "] * (n*2) for _ in range(n)]


def go(tx, ty, bottom_x, ly, ry, n):

    if n == 6:
        for i in range(3):
            for j in range(i+1):
                if i == 1 and j == 0:
                    continue
                nx = tx + i
                ny = ty + j
                ny2 = ty - j
                map[nx][ny] = "*"
                map[nx][ny2] = "*"
        return

    bottom_y = ty

    mid_x = ((tx+bottom_x) // 2) + 1

    left_y = ly + ((ty-ly) // 2) + 1

    right_y = ty + ((ry-ty) // 2)

    go(tx, ty, mid_x-1, left_y, right_y, n//2) # 위쪽

    go(mid_x, left_y-1, bottom_x, ly, bottom_y-1, n//2) # 왼쪽

    go(mid_x, right_y + 1, bottom_x, bottom_y + 1, ry, n//2) # 오른쪽


go(0, n-1, n-1, 0, (n*2)-2, n*2)

for i in range(n):
    print(*map[i],  sep="")