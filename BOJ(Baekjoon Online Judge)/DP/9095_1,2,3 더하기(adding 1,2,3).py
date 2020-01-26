#https://www.acmicpc.net/problem/9095

import sys

# Bottom-up

T = int(sys.stdin.readline())

d = [0] * 11
d[0] = d[1] = 1
d[2] = 2

for i in range(T):
    n = int(sys.stdin.readline())
    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])
"""
# Top-down
def dp(n):
    if n <= 2:
        if n <= 1:
            return 1
        else:
            return 2
    if d[n] > 0:
        return d[n]

    d[n] = dp(n-1) + dp(n-2) + dp(n-3)
    return d[n]

T = int(sys.stdin.readline())
for i in range(T):
    d = [0] * 11
    d[0] = d[1] = 1
    d[2] = 2
    n = int(sys.stdin.readline())
    print(dp(n))
"""