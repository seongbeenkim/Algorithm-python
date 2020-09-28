#https://www.acmicpc.net/problem/14395

import sys
from collections import deque

s, t = map(int,sys.stdin.readline().split())
op = ['*','+','-','/']
limit = 2*(10**9)
check = set()
q = deque()
q.append((s,""))
check.add(s)
is_answer = False
if s == t:
    is_answer = True
    print(0)
else:
    while q:
        x, ans = q.popleft()
        if x == t:
            print(ans)
            is_answer = True
            break
        for k in op:
            nx = x
            if k == '*':
                nx *= nx
            elif k == '+':
                nx += nx
            elif k == '-':
                nx -= nx
            else:
                if nx > 0:
                    nx //= nx

            if 0 <= nx < limit and not nx in check:
                check.add(nx)
                q.append((nx,ans + k))

if not is_answer:
    print(-1)