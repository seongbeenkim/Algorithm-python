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