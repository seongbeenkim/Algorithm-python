#https://www.acmicpc.net/problem/1918

import sys

arr = sys.stdin.readline().rstrip()

op = []
ans = []
op_priority = {"-" : 1, "+" : 1, "*" : 2, "/" : 2, "(" : 0}

for i in arr:
    if 65 <= ord(i) <= 90:
        ans.append(i)
    elif i == "(":
        op.append(i)
    elif i == ")":
        while op and op[-1] != "(":
            ans.append(op.pop())
        op.pop()
    else:
        while op and op_priority[i] <= op_priority[op[-1]]:
            ans.append(op.pop())
        op.append(i)

while op:
    ans.append(op.pop())
print("".join(ans))