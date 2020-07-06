#https://www.acmicpc.net/problem/10799

import sys

a = sys.stdin.readline().rstrip()
ans = 0
stack = []
is_split = False

for i in a:
    if i == "(":
        stack.append(i)
        is_split = False

    else:
        if stack[-1] == "(" and i == ")" and is_split == True:
            stack.pop()
            ans += 1
        elif stack[-1] == "(" and i == ")" and is_split == False:
            stack.pop()
            ans += len(stack)
            is_split = True

print(ans)