#https://www.acmicpc.net/problem/15665

import sys
from collections import Counter
n,m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
a = list(Counter(a).items())
num, cnt = map(list,zip(*a))
ans = [0] * m

def go(index,cnt,num,a):
    if index == m:
        print(*ans)
        return
    for i in range(len(cnt)):
        ans[index] = num[i]
        go(index+1,cnt,num,a)
go(0,cnt,num,a)

"""
ans = []
def go(index,seq):
    if index == m:
        ans.append(tuple(seq))
        return
    for i in range(n):
        go(index+1,seq+[a[i]])
go(0,[])
ans = sorted(list(set(ans)))
for v in ans:
    print(*v)
"""

"""
n, m = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

candi = []
def go(index,ans):
    global candi
    if len(ans) == m:
        candi.append(tuple(ans))
        return

    if index >= n:
        return

    for i in range(n):
        go(index+1,ans + [a[i]])
go(0,[])
ans = list(set(candi))
ans.sort()
for i in ans:
    print(*i)
"""