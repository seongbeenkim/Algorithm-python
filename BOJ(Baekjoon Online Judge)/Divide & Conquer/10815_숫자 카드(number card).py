#https://www.acmicpc.net/problem/10815

import sys

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

ans = []
card.sort()

def go(num):
    left = 0
    right = len(card)-1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if card[mid] == num:
            ans.append(1)
            return
        elif card[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    ans.append(0)
for x in numbers:
    go(x)
for x in ans:
    print(x , end = " ")