#acmicpc.net/problem/2042

import sys
from math import ceil, log

n, m, k = map(int,sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for _ in range(n)]
h = ceil(log(n,2))
tree_size = (1<<(h+1))
INF = 10**9
tree = [INF] * tree_size

def init(node,start,end):
    if start == end:
        tree[node] = num[start]
    else:
        mid = (start+end)//2
        init(node*2,start,mid)
        init(node*2+1,mid+1,end)
        tree[node] = (tree[node*2]+tree[node*2+1])
init(1,0,n-1)

def query(node,start,end,i,j):
    if i<=start and end<=j:
        return tree[node]
    if end < i or j < start:
        return -1
    mid = (start+end)//2
    m1 = query(node*2,start,mid,i,j)
    m2 = query(node*2+1,mid+1,end,i,j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return m1+m2

def update(node,start,end,index,diff):
    if index < start or end < index:
        return -1
    tree[node] += diff
    if start != end:
        mid = (start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

for i in range(m+k):
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1:
        diff = c - num[b-1]
        num[b-1] = c
        update(1,0,n-1,b-1,diff)
    else:
        print(query(1,0,n-1,b - 1, c - 1))