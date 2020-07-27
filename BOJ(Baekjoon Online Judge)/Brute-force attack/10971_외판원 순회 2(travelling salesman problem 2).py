#https://www.acmicpc.net/problem/10971

import sys

n = int(sys.stdin.readline())
w = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
m = 2147483647
d = list(range(n))

def next_permutation(a):

    i = len(a) - 1
    while i > 0 and a[i] <= a[i-1]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

while True:
    if d[0] != 0: # (0 -> 1 -> 2 -> 3) == (1 -> 2 -> 3 -> 0) == (2 -> 3 -> 0 -> 1) == (3 -> 0 -> 1 -> 2) 이기 때문에 앞에 0인 경우의 수만 하면 조금 더 빠르다
        break
    ok = True
    s = 0
    for i in range(0, n-1):
        if w[d[i]][d[i+1]] == 0:
            ok = False
            break
        else:
            s += w[d[i]][d[i+1]]
    if ok and w[d[-1]][d[0]] != 0:
        s += w[d[-1]][d[0]]
        m = min(m, s)
    if not next_permutation(d):
        break
print(m)

"""
a = list(range(n))
minimum = 2147483647
while True:
    end = a[0]
    res = 0
    is_blocked = False
    for i in range(n):
        if i == n-1:
            if w[a[i]][end] == 0:
                is_blocked = True
                break
            res += w[a[i]][end]
        else:
            if w[a[i]][a[i+1]] == 0:
                is_blocked = True
                break
            res += w[a[i]][a[i+1]]
    if not is_blocked:
        minimum = min(minimum,res)
    if not next_permutation():
        break
"""