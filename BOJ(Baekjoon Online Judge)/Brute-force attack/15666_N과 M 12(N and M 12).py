#https://www.acmicpc.net/problem/15666

import sys

n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
ans = []

def go(index,start,a,seq):
    if index == m:
        ans.append(tuple(seq))
        return
    for i in range(start,len(a)):
        go(index + 1, i,a,seq+[a[i]])
go(0,0,a,[])
ans = sorted(list(set(ans)))
for x in ans:
    print(*x)

"""
a = list(set(map(int,sys.stdin.readline().split())))
a.sort()
ans = [0] * m

def go(index,start,a):
    if index == m:
        print(*ans)
        return
    for i in range(start,len(a)):
        ans[index] = a[i]
        go(index + 1, i,a)
go(0,0,a)
"""

"""
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

candi = []
def go(index,start,ans):
    global candi
    if len(ans) == m:
        candi.append(tuple(ans))
        return

    if index >= n:
        return

    for i in range(start,n):
        go(index+1,i,ans + [a[i]])
go(0,0,[])
ans = list(set(candi))
ans.sort()
for i in ans:
    print(*i)
"""