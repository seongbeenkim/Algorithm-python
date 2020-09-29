#https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort()
for i in a:
    print(*i)