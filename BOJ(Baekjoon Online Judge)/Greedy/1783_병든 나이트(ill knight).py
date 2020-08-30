#https://www.acmicpc.net/problem/1783

import sys

n, m = map(int, sys.stdin.readline().split())

if n == 1:
    print(1)

elif n == 2:
    print(min(4,(m+1)//2))

else:
    if m >= 7:
        print(m-7 + 5)
    else:
        print(min(4,m))