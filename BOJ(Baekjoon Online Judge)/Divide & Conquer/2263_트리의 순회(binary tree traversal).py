#https://www.acmicpc.net/problem/2263

import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
in_order = list(map(int,sys.stdin.readline().split()))
post_order = list(map(int,sys.stdin.readline().split()))
position = [0] * (n+1)

for i in range(n):
    position[in_order[i]] = i

def go(in_start,in_end,post_start,post_end):

    if in_start > in_end and post_start > post_end:
        return

    root = post_order[post_end] # 현재 root 값
    print(root, end=" ")
    p = position[root] # root 값에 대한 in_order의 index
    left = p - in_start

    go(in_start, p-1, post_start, post_start + left - 1) # left
    go(p+1, in_end, post_start + left, post_end-1) # right

go(0,n-1,0,n-1)