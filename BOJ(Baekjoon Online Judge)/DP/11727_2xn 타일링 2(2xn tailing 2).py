#https://www.acmicpc.net/problem/11727

import sys
sys.setrecursionlimit(10**6)

# Bottom-up

n = int(sys.stdin.readline())
d = [0] * (n+1)
d[0] = d[1] = 1

for i in range(2,n+1):
    d[i] = (d[i-1] + 2*d[i-2])%10007
print(d[n])

# Top-down
"""
def dp(n):
    if n <= 1:
        return 1
    if d[n] > 0:
        return d[n]

    d[n] = (dp(n-1) + 2*dp(n-2))%10007
    return d[n]


n = int(sys.stdin.readline())
d = [0] * (n+1)
d[0] = d[1] = 1
print(dp(n))
"""