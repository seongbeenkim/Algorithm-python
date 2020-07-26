#https://www.acmicpc.net/problem/10819

import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort() # 모든 순열을 위해서 필수

def next_permutation():
    i = n-1
    while i>0 and a[i] < a[i-1]:
        i -= 1
    if i == 0:
        return False
    j = n - 1

    while a[i-1] > a[j]:
        j-=1
    a[i-1],a[j] = a[j],a[i-1]
    j = n - 1
    while i<j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return True
ans = 0
while True:
    res = 0
    for i in range(1,n):
        res += abs(a[i-1] - a[i])
    ans = max(ans,res)
    if not next_permutation():
        break
print(ans)