#https://www.acmicpc.net/problem/2875

import sys

n,m,k = map(int,sys.stdin.readline().split())

if n%2 == 1 and k > 0:
    k -= 1
    n -= 1

while k > 0:
    if n > m*2:
        n -= 1
    else:
        m -= 1
    k -= 1

n = n//2
if n == 0 or m == 0:
    print(0)
else:
    if n == m:
        print(m)
    elif n > m:
        print(m)
    elif n < m:
        print(n)