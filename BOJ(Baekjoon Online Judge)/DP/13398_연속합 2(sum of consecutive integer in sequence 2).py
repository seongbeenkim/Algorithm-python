#https://www.acmicpc.net/problem/13398

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [[0]*2 for _ in range(n)]
d[0][0] = a[0]
d[0][1] = -100000001

for i in range(1,n):
    d[i][0] = max(d[i-1][0] + a[i], a[i])
    d[i][1] = max(d[i-1][0],d[i-1][1]+a[i])

ans = -100000001
for a,b in d:
    ans = max(a,b,ans)
print(ans)