#https://www.acmicpc.net/problem/11664

import sys
from math import sqrt

ax, ay, az, bx, by, bz, cx, cy, cz = map(int,sys.stdin.readline().split())

lx = ax
rx = bx

ly = ay
ry = by

lz = az
rz = bz

ans = 2147483647


while True:
    mx = (lx + rx) / 2
    my = (ly + ry) / 2
    mz = (lz + rz) / 2

    l = sqrt((lx-cx)**2 + (ly-cy)**2 + (lz-cz)**2)
    h = sqrt((mx-cx)**2 + (my-cy)**2 + (mz-cz)**2)
    r = sqrt((rx-cx)**2 + (ry-cy)**2 + (rz-cz)**2)

    if (abs(h - ans) <= 0.00000000001):
        break

    if h < ans:
        ans = h

    if l > r:
        lx = mx
        ly = my
        lz = mz

    else:
        rx = mx
        ry = my
        rz = mz

print("{:.10f}".format(ans))