#https://www.acmicpc.net/problem/1654

import sys

k,n = map(int,sys.stdin.readline().split())
a = []
for i in range(k):
    a.append(int(sys.stdin.readline()))

def check(num):
    cnt = 0
    for i in a:
        cnt += i // num
    return cnt

l = 1
r = max(a)

while l <= r:
    m = (l+r) // 2
    res = check(m)
    if res >= n:
        l = m+1
    else:
        r = m-1
print(r)