#https://www.acmicpc.net/problem/11651

import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a.sort(key = lambda x : [x[1],[0]])
for i in a:
    print(*i)