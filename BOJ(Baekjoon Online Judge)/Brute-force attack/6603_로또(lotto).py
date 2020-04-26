#https://www.acmicpc.net/problem/6603

import sys
def go(i,lotto):
    if len(lotto) == 6:
        print(*lotto)
        return
    if i >= len(s):
        return
    go(i+1,lotto+[s[i]])
    go(i+1,lotto)

while True:
    k, *s = list(map(int,sys.stdin.readline().split()))
    if k == 0:
        break
    go(0,[])
    print()

""" 
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i == 0:
        return False
    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1] , a[j] = a[j], a[i-1]
    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return True
while True:
    k, *s = map(int,sys.stdin.readline().split())
    if k == 0:
        break
    ans = []
    d = [0] * (k - 6) + [1] * 6
    while True:
        cur = [s[i] for i in range(k) if d[i] == 1]
        ans.append(cur)
        if not next_permutation(d):
            break
    ans.sort()
    for i in ans:
        print(" ".join(map(str,i)))
    print()
"""