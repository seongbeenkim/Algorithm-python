#https://www.acmicpc.net/problem/17413

import sys

S = sys.stdin.readline().rstrip()

reversed_S = []
is_tag = False

for i in S:
    if i == "<":
        is_tag = True
        while reversed_S:
            x = reversed_S.pop()
            print(x,end = "")
        print(i, end="")
        continue

    elif i == ">":
        is_tag = False
        print(i, end="")
        continue

    if is_tag == False:
        if i != " ":
            reversed_S.append(i)
        else:
            while reversed_S:
                x = reversed_S.pop()
                print(x, end="")
            print(" ",end = "")
    else:
        print(i,end = "")
print("".join(reversed_S[-1::-1]))