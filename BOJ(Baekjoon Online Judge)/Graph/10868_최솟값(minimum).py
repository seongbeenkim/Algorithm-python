#https://www.acmicpc.net/problem/10868

import sys
from math import ceil, log

n, m = map(int,sys.stdin.readline().split())
h = int(ceil(log(n,2)))
size = (1<<(h+1))
tree = [1000000001] * size
a = list(int(sys.stdin.readline().rstrip()) for i in range(n))

def init(node,start,end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node] = min(tree[node*2],tree[node*2+1])

init(1,0,n-1)
def query(node,start,end,i,j):
    if start > j or end < i:
        return -1
    if i<=start and end<=j:
        return tree[node]
    mid = (start+end)//2
    m1 = query(node*2,start,mid,i,j)
    m2 = query(node*2+1,mid+1,end,i,j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return min(m1,m2)

for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    print(query(1,0,n-1,i-1,j-1))