#https://www.acmicpc.net/problem/2357

import sys
from math import ceil, log

n, m = map(int,sys.stdin.readline().split())
h = int(ceil(log(n,2)))
tree_size = (1<<(h+1))
min_tree = [1000000001] * tree_size
max_tree = [1000000001] * tree_size
a = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def initMin(node,start,end):
    if start == end:
        min_tree[node] = a[start]
        max_tree[node] = a[start]
    else:
        mid = (start+end)//2
        initMin(node*2,start,mid)
        initMin(node*2+1,mid+1,end)
        min_tree[node] = min(min_tree[node*2],min_tree[node*2+1])
        max_tree[node] = max(max_tree[node*2],max_tree[node*2+1])
initMin(1,0,n-1)

def min_query(node,start,end,i,j):
    if i <= start and end <= j:
        return min_tree[node]
    if end < i or j < start:
        return -1
    mid = (start+end) // 2
    m1 = min_query(node*2,start,mid,i,j)
    m2 = min_query(node*2+1,mid+1,end,i,j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return min(m1,m2)

def max_query(node,start,end,i,j):
    if i <= start and end <= j:
        return max_tree[node]
    if end < i or j < start:
        return -1
    mid = (start+end) // 2
    m1 = max_query(node*2,start,mid,i,j)
    m2 = max_query(node*2+1,mid+1,end,i,j)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return max(m1,m2)

for _ in range(m):
    s, e = map(int,sys.stdin.readline().split())
    print(min_query(1,0,n-1,s-1,e-1),max_query(1,0,n-1,s-1,e-1))
