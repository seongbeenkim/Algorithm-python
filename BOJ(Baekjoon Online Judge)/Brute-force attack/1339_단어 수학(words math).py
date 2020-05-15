#https://www.acmicpc.net/problem/1339

import sys

n = int(sys.stdin.readline())
a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ans = 0
alphabet = [0] * 26

for li in a:
    i = len(li)-1
    for alpha in li:
        alphabet[ord(alpha)-ord("A")] += 10**i
        i-=1
alphabet.sort(reverse=True)
for i in range(9,0,-1):
    ans += i*alphabet[9-i]
print(ans)