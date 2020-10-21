#https://www.acmicpc.net/problem/3019

import sys

c, p = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
answer = 0

def cal(i, s):
    if i + len(s)-1 >= c:
        return 0
    base = a[i] - (ord(s[0]) - ord('0'))
    for j in range(len(s)):
        if base != a[i+j] - (ord(s[j]) - ord('0')):
            return 0
    return 1

for i in range(c):
    if p == 1:
        answer += cal(i,"0") + cal(i,"0000")
    elif p == 2:
        answer += cal(i,"00")
    elif p == 3:
        answer += cal(i,"001") + cal(i,"10")
    elif p == 4:
        answer += cal(i,"100") + cal(i,"01")
    elif p == 5:
        answer += cal(i,"000") + cal(i,"10") + cal(i,"01") + cal(i,"101")
    elif p == 6:
        answer += cal(i,"000") + cal(i,"00") + cal(i,"011") + cal(i,"20")
    elif p == 7:
        answer += cal(i,"000") + cal(i,"02") + cal(i,"110") + cal(i,"00")

print(answer)