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

def go(arr,cnt):

    for i in range(1,n):
        if arr[i-1] != result[i-1]:
            switch(i,arr)
            cnt += 1

    if arr == result:
        return cnt
    else:
        return -1

clicked_cnt = go(clicked,1)
unclicked_cnt = go(a,0)

if result == clicked and result == a:
    print(min(clicked_cnt,unclicked_cnt))
elif result == clicked:
    print(clicked_cnt)
elif result == a:
    print(unclicked_cnt)
elif result != clicked and result != a:
    print(-1)

"""
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().rstrip()))
b = list(map(int,sys.stdin.readline().rstrip()))

copy_a = a.copy()
copy_a[0] = 1 - copy_a[0]
copy_a[1] = 1 - copy_a[1]

def count(a):
    cnt = 0
    for i in range(1,n):
        if a[i-1] != b[i-1]:
            if i == n-1:
                a[n-1] = 1 - a[n-1]
                a[n-2] = 1 - a[n-2]
            else:
                a[i-1] = 1 - a[i-1]
                a[i] = 1 - a[i]
                a[i+1] = 1 - a[i+1]
            cnt += 1

    for i in range(n):
        if a[i] != b[i]:
            cnt = -1
    return cnt

res = count(a)
res_2 = count(copy_a)
ans = -1
if res != -1 and res_2 != -1:
    ans = min(res,res_2+1)
elif res == -1 and res_2 != -1:
    ans = res_2+1
elif res_2 == -1 and res != -1:
    ans = res
print(ans)

"""