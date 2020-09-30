#https://www.acmicpc.net/problem/11652

import sys

n = int(sys.stdin.readline())
d = {}

for i in range(n):
    x = int(sys.stdin.readline())
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

ans = sorted(d.items(), key = lambda x : (-x[1],-x[0]))

maximum = ans[0][1]
answer = ans[0][0]

for i in range(1,len(ans)):
    if ans[i][1] == maximum:
        answer = ans[i][0]
    else:
        break
print(answer)