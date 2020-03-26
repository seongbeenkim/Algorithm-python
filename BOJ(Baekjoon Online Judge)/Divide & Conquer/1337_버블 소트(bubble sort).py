#https://www.acmicpc.net/problem/1377

import sys

n= int(sys.stdin.readline())
a = []
for i in range(n):
    x = int(sys.stdin.readline())
    a.append((x,i))
ans = 0
a.sort()
for i in range(n):
    if a[i][1] - i > ans:
        ans = a[i][1] - i

print(ans+1)