#https://www.acmicpc.net/problem/1182

import sys

n, s = map(int,sys.stdin.readline().split())
k = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(1, 1<<n):
    sum = 0
    for j in range(0,n):
        if i & (1<<j):
            sum += k[j]
    if sum == s:
       cnt += 1

print(cnt)

"""
import sys

def go(index,sum):

    global cnt
    if index == n:
        if sum == s:
            cnt += 1
        return
    go(index+1,sum+k[index])
    go(index+1,sum)

go(0,0)
if s == 0:
    cnt -= 1
print(cnt)
"""