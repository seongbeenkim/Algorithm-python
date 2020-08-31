#https://www.acmicpc.net/problem/1786

import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

fail = [0] * len(P)
n = len(T)
m = len(P)

def pre_processing():
    j = 0
    for i in range(1,m):
        while j > 0 and P[i] != P[j]:
            j = fail[j-1]
        if P[i] == P[j]:
            fail[i] = j+1
            j += 1
        else:
            fail[i] = 0

def kmp():
    j = 0
    ans = []
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = fail[j-1]
        if T[i] == P[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = fail[j]
            else:
                j += 1

    return ans

pre_processing()
ans = kmp()

print(len(ans))
for i in ans:
    print(i+1)

"""
t = list(sys.stdin.readline().rstrip())
p = list(sys.stdin.readline().rstrip())

pi = [0] * len(p)
t_pi = [0] * len(t)

for i in range(1,len(p)):
    j=i

    while pi[j-1] != 0 and p[i] != p[pi[j-1]]:
        j = pi[j-1]
    if pi[j-1] == 0:
        if p[i] == p[0]:
            pi[i] = 1

    if p[i] == p[pi[j-1]]:
        pi[i] = pi[j-1] + 1

j = 0
for i in range(len(t)):

    while j > 0 and t[i] != p[j]:
        j = pi[j-1]

    if j == 0:
        if t[i] == p[j]:
            t_pi[i] = 1
            j += 1
    else:
        if t[i] == p[j]:
            t_pi[i] = j + 1
            j += 1
            if j == len(p):
                j = 0
ans = []
for i in range(len(t_pi)):
    if t_pi[i] == len(p):
        ans.append((i+1)-len(p)+1)
print(len(ans))
for i in ans:
    print(i)
"""