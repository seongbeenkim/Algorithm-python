#https://www.acmicpc.net/problem/2138

import sys, copy
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().rstrip()))
result = list(map(int,sys.stdin.readline().rstrip()))

clicked = copy.deepcopy(a)

clicked[0] ^= 1
clicked[1] ^= 1

def switch(x,s):

    if x < n - 1:
        s[x] ^= 1
        s[x - 1] ^= 1
        s[x + 1] ^= 1

    elif x == n - 1:
        s[x] ^= 1
        s[x - 1] ^= 1

def go(x,arr,cnt):

    if x == n:
        return cnt

    if result[x-1] == arr[x-1]:
        cnt = go(x+1,arr,cnt)
    else:
        switch(x,arr)
        cnt = go(x+1,arr,cnt+1)

    return cnt

clicked_cnt = go(1,clicked,1)
unclicked_cnt = go(1,a,0)

if result == clicked and result == a:
    print(min(clicked_cnt,unclicked_cnt))
elif result == clicked:
    print(clicked_cnt)
elif result == a:
    print(unclicked_cnt)
elif result != clicked and result != a:
    print(-1)