#https://www.acmicpc.net/problem/10825

import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    n, k, e, s = sys.stdin.readline().split()
    a.append([n,int(k),int(e),int(s)])

a.sort(key = lambda x : [-x[1],x[2],-x[3],x[0]])

for i in a:
    print(*i)

print(ord('n'),ord('W'),ord('S'))