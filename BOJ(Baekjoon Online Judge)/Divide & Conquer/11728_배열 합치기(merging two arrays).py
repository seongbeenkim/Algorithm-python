#https://www.acmicpc.net/problem/11728

import sys

n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
ans = [0] * (n+m)

i = 0
j = 0
k = 0

while i < n and j < m:
    if a[i] <= b[j]:
        ans[k] = a[i]
        k+=1
        i+=1
    else:
        ans[k] = b[j]
        k += 1
        j += 1
while i < n:
    ans[k] = a[i]
    k += 1
    i += 1
while j < m:
    ans[k] = b[j]
    k += 1
    j += 1

print(" ".join(str(i) for i in ans))