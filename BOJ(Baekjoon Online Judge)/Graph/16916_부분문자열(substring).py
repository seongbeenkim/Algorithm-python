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
            hash_s = (hash_s + mod) % mod
            hash_s = ((hash_s * base) % mod + ord(s[i+m])) % mod
    return 0

print(match(s,p))