#https://www.acmicpc.net/problem/14889

import sys

n = int(sys.stdin.readline())
s = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
ans = 2147483647
for i in range(1 << ((n//2)-1), 1<<n): # (1,1<<n)으로 해도 상관 x
    start = []
    link = []
    for j in range(n):
        if i & (1 << j):
            start += [j]
        else:
            link += [j]
    if len(start) != n//2:
        continue

    start_sum = 0
    link_sum = 0

    for k in range((n//2)-1):
        for l in range(k+1,n//2):

            start_sum += s[start[k]][start[l]] + s[start[l]][start[k]]

            link_sum += s[link[k]][link[l]] + s[link[l]][link[k]]

    res = abs(start_sum - link_sum)
    if ans > res:
        ans = res
print(ans)


"""
def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i+=1
        j-=1
    return True

n = int(sys.stdin.readline())
s = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a = []
for i in range(n//2):
    a.append(0)
for i in range(n//2,n):
    a.append(1)

ans = 100*20*20
while True:
    first_team = []
    second_team = []
    first = 0
    second = 0
    for i in range(n):
        if a[i] > 0:
            first_team.append(i)
        else:
            second_team.append(i)

    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue
            first += s[first_team[i]][first_team[j]]
            second += s[second_team[i]][second_team[j]]

    ans = min(abs(first-second),ans)
    if not next_permutation(a):
        break
print(ans)
"""


"""
n = int(sys.stdin.readline())
s = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def go(index,first,second):
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        f1 = 0
        f2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                f1 += s[first[i]][first[j]]
                f2 += s[second[i]][second[j]]
        return abs(f1-f2)
    ans = 100*20*20
    t1 = go(index+1,first+[index],second)
    if t1 != -1:
        ans = min(ans,t1)
    t2 = go(index+1,first,second+[index])
    if t2 != -1:
        ans = min(ans,t2)
    return ans

print(go(0,[],[]))

"""