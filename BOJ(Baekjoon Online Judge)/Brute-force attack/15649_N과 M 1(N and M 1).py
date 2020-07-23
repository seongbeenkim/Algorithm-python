#https://www.acmicpc.net/problem/15649
import sys

n, m = map(int,sys.stdin.readline().split())
c = [False]* (n+1)
a = [0] * m

def go(index,n,m):
    if index == m:
        sys.stdout.write(" ".join(map(str,a)) + "\n" )
        return

    for i in range(1,n+1):
        if c[i] == True:
            continue
        c[i] = True
        a[index] = i
        go(index+1,n,m)
        c[i] = False

go(0,n,m)

"""
n, m = map(int,sys.stdin.readline().split())

def go(index,candi):

    if len(candi) == m:
        print(*candi)
        return

    for i in range(1,n+1):
        if i not in candi:
            go(index,candi+[i])

for i in range(1,n+1):
    go(i,[i])
"""