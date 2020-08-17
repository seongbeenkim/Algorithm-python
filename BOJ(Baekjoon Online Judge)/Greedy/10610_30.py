#https://www.acmicpc.net/problem/10610

import sys
n = sys.stdin.readline().rstrip()

total = 0
res = []
ans = ''
for i in n:
    res.append(i)
    total += int(i)

if total % 3 == 0:
    res.sort()
    if res[0] == '0':
        res.reverse()
        for i in res:
            ans += i
        print(ans)
    else:
        print(-1)
else:
    print(-1)



"""
n = list(sys.stdin.readline().rstrip())

ans = 0
is_answer = True

if '0' not in n:
    print(-1)
else:
    n.sort(reverse=True)
    for i in n:
        ans += int(i)
    
    if ans % 3 != 0:
        print(-1)
    else:
        print(*n,sep="")
"""

