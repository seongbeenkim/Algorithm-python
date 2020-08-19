#https://www.acmicpc.net/problem/4256

import sys

t = int(sys.stdin.readline())

def go(in_start,in_end,pre_start,pre_end):

    if in_start > in_end or pre_start > pre_end:
        return

    root = pre_order[pre_start] # root

    p = position[root] # root 값인 in_order의 index

    left = p - in_start

    go(in_start, p-1, pre_start+1, pre_start+left) # left
    go(p+1, in_end, pre_start+left+1, pre_end) # right
    print(root, end = " ") # 후위 출력

for _ in range(t):
    n = int(sys.stdin.readline())
    pre_order = list(map(int,sys.stdin.readline().split()))
    in_order = list(map(int,sys.stdin.readline().split()))
    position = [0] * (n+1)

    for i in range(n):
        position[in_order[i]] = i
    go(0,n-1,0,n-1)