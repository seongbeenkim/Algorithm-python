#https://www.acmicpc.net/problem/1517

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
arr = [0] * n
cnt = 0
def merge(start,mid,end):
    global cnt
    l = start
    r = mid + 1
    k = start
    while l <= mid and r <= end:
        if a[l] > a[r]:
            arr[k] = a[r]
            k += 1
            r += 1
            cnt += mid-l+1
        else:
            arr[k] = a[l]
            k+=1
            l += 1
    while l <= mid:
        arr[k] = a[l]
        k += 1
        l += 1
    while r <= end:
        arr[k] = a[r]
        k += 1
        r += 1


    for i in range(start,end+1):
        a[i] = arr[i]

def split(start,end):
    if start == end:
        return
    mid = (start+end) // 2
    split(start,mid)
    split(mid+1,end)
    merge(start,mid,end)

split(0,len(a)-1)
print(cnt)


"""
def merge(start,mid,end):
    global cnt
    i = start
    j = mid+1
    k = start
    plus = 0

    while i <= mid and j <= end:
        if a[i] > a[j]:
            ans[k] = a[j]
            j += 1
            plus += 1

        elif a[i] <= a[j]:
            ans[k] = a[i]
            i += 1
            cnt += plus

        k += 1

    while i <= mid:
        ans[k] = a[i]
        i += 1
        k += 1
        cnt += plus

    while j <= end:
        ans[k] = a[j]
        j += 1
        k += 1

    for i in range(start,end+1):
        a[i] = ans[i]
"""