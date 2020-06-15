#https://www.acmicpc.net/problem/11058

import sys

n = int(sys.stdin.readline())
d = [0] * (n+1)

for i in range(1,n+1):
    if i <= 6:
        d[i] = i
    else:
        d[i] = max(d[i-5] * 4, d[i-4] * 3, d[i-3] * 2)
print(d[n])

"""
for i in range(1,n+1):
    d[i] = d[i-1] + 1
    for j in range(1, i-3+1):
        cur = d[i-(j+2)]*(j+1)
        if cur > d[i]:
            d[i] = cur
"""