#https://www.acmicpc.net/problem/1463

import sys

# Bottom-up
n = int(sys.stdin.readline())
d = [0] * (n+1)
d[0] = d[1] = 0

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
print(d[n])

# Top-down
""" 
sys.setrecursionlimit(10**6)

def dp(n):

    if n <= 1:
        return 0

    if d[n] > 0:
        return d[n]

    d[n]= dp(n - 1) + 1

    if n % 3 == 0:
        temp = dp(n//3) + 1
        if temp < d[n]:
            d[n] = temp

    if n % 2 == 0:
        temp = dp(n//2) + 1
        if temp < d[n]:
            d[n] = temp
    return d[n]

n = int(sys.stdin.readline())
d = [0] * (n+1)
print(dp(n))
"""
# Top-down 2
"""
def dp(n):

    temp = 1000000

    if n <= 1:
        return 0

    if d[n] > 0:
        return d[n]

    if n % 3 == 0:
        temp = min(temp,dp(n//3) + 1)

    if n % 2 == 0:
        temp = min(temp,dp(n//2) + 1)

    d[n] = min(temp, dp(n-1) + 1)
    return d[n]
"""
