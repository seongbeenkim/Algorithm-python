#https://www.acmicpc.net/problem/2156

import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
d = [0] * n
d[0] = a[0]
if n > 1:
    d[1] = a[0] + a[1]

    for i in range(2,n):
        d[i] = max(d[i-1],d[i-2]+a[i],d[i-3]+a[i-1]+a[i])
print(d[n-1])
"""
d = [[0] * 3 for _ in range(n)]
d[0][1] = a[0]
for i in range(1,n):
    d[i][0] = max(d[i-1])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]
print(max(d[n-1]))
"""

"""
n = int(sys.stdin.readline())
a = [0] + [int(sys.stdin.readline()) for _ in range(n)]
d = [[0] * 3 for _ in range(n+1)]
d[1][1] = a[1]

if n >= 2:
    d[2][0] = a[1]
    d[2][1] = a[2]
    d[2][2] = a[1] + a[2]
    for i in range(3,n+1):
        d[i][0] = max(d[i-1])
        d[i][1] = d[i-1][0] + a[i]
        d[i][2] = d[i-1][1] + a[i]

print(max(d[n]))
"""
