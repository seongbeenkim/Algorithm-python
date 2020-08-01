#https://www.acmicpc.net/problem/10815

import sys, bisect
from collections import Counter

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

card.sort()
### solve 1
"""
def lower_bound(num):
    left = 0
    right = len(card)-1
    mid = 0
    ans = -1
    while left <= right:
        mid = (mid + right) // 2
        if card[mid] == num:
            ans = mid
            right = mid - 1
        elif card[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return ans

def upper_bound(num):
    left = 0
    right = len(card) - 1
    mid = 0
    ans = -1
    while left <= right:
        mid = (left+right) // 2
        if card[mid] == num:
            ans = mid + 1
            left = mid+1
        elif card[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return ans

for x in numbers:
    l = lower_bound(x)
    u = upper_bound(x)
    if l == -1:
        print(0, end= " ")
    else:
        print(u-l, end = " ")
"""

### solve 2
"""
counter = Counter(card)
res = [0] * m
for x in numbers:
    if x in counter:
        print(counter[x] , end = " ")
    else:
        print(0, end = " ") 
"""

### solve 3
for i in range(m):
    idx = bisect.bisect_left(card,numbers[i])
    if idx < len(card) and card[idx] == numbers[i]:
        idx2 = bisect.bisect(card,numbers[i])
        print(idx2-idx, end = " ")
    else:
        print(0, end = " ")


# solve 4, but solve 1과 같은데 solve 1은 시간 초과
"""
n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
card.sort()
m = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

def lower_bound(left,right,num):
    ans =-1
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == num:
            ans = mid
            right = mid - 1

        elif card[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return ans
def upper_bound(left,right,num):
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == num:
            ans = mid + 1
            left = mid + 1

        elif card[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return ans

for i in range(m):
    l = lower_bound(0,n-1,numbers[i])
    r = upper_bound(0,n-1,numbers[i])
    if l == -1:
        print(0, end = " ")
    else:
        print(r-l, end = " ")

"""