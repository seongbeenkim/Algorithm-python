#https://www.acmicpc.net/problem/10814

import sys

n = int(sys.stdin.readline())
ans = {}
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    if age not in ans:
        ans[age] = []
        ans[age].append(name)
    else:
        ans[age].append(name)

answer = sorted(ans.items(), key = lambda x : x[0])
for i in answer:
    if len(i[1]) > 1:
        m = 0
        while m < len(i[1]):
            print(i[0], i[1][m])
            m += 1
    else:
        print(i[0], i[1][0])