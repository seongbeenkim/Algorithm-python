#https://www.acmicpc.net/problem/2805

import sys

n, m = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

h = max(trees)

def cut(h):
    leftover = 0
    for tree in trees:
        piece = tree - h
        if piece > 0:
            leftover += piece
    return leftover >= m

i = 1
j = h
ans = 0
while i <= j:
    mid = (i+j) // 2
    if cut(mid):
        ans = max(mid,ans)
        i = mid + 1
    else:
        j = mid - 1

print(ans)