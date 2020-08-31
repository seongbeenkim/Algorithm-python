#https://www.acmicpc.net/problem/16916

import sys

mod = 127
base = 256
s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()

def h(s):
    ans = 0
    for ch in s:
        ans = (ans * base + ord(ch)) % mod
    return ans

def match(s,p):
    n = len(s)
    m = len(p)
    if n < m:
        return 0
    hash_s = h(s[0:m])
    hash_p = h(p)

    first = 1
    for i in range(m-1):
        first = (first * base) % mod
    for i in range((n-m)+1):
        if hash_p == hash_s:
            if s[i:i+m] == p:
                return 1
        if i+m < n:
            hash_s = hash_s - (ord(s[i])*first) % mod
            hash_s = ((hash_s * base) % mod + ord(s[i+m])) % mod
    return 0

print(match(s,p))


"""
s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
pi = [0] * len(p)

def get_pi():
    n = len(p)
    j = 0
    for i in range(1,n):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j+1
            j += 1
        else:
            pi[i] = 0
get_pi()

def check():
    n = len(s)
    j = 0
    ans = []
    for i in range(n):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == len(p)-1:
                ans.append(i-len(p)+1)
                j = pi[j]
            else:
                j += 1
    return ans
res = check()
if len(res) > 0:
    print(1)
else:
    print(0)
"""

"""
pattern = [0] * len(p)
s_pattern = [0] * len(s)

for i in range(1,len(p)):
    j = i

    while pattern[j-1] != 0 and p[pattern[j-1]] != p[i]:
        j = pattern[j-1]

    if pattern[i-1] == 0:
        if p[i] == p[0]:
            pattern[i] = 1

    if p[pattern[j-1]] == p[i]:
        pattern[i] = pattern[j-1] + 1

j = 0
for i in range(len(s)):

    while j > 0 and s[i] != p[j]:
        j = pattern[j-1]

    if j == 0:
        if p[j] == s[i]:
            s_pattern[i] = 1
            j += 1
    else:
        if p[j] == s[i]:
            s_pattern[i] = j + 1
            j += 1
            if j == len(p):
                j = pattern[j-1]
ans = 0
for i in s_pattern:
    if i == len(p):
        ans = 1
        break
print(ans)
"""