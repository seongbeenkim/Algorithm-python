#https://www.acmicpc.net/problem/2022

import sys, math

x, y, c = map(float,sys.stdin.readline().split())

l = 0
r = min(x,y)

ans = 0
while abs(r-l) >= 1e-6:
    mid = (l+r) / 2.0
    d = mid
    h1 = math.sqrt((x*x) - (d*d))
    h2 = math.sqrt((y*y) - (d*d))
    h = (h1*h2) / (h1+h2)
    if h > c:
        l = mid
    else:
        r = mid
        ans = mid

print("{}".format(round(ans,3)))