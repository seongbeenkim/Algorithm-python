#https://www.acmicpc.net/problem/9935

import sys

string = sys.stdin.readline().rstrip()
explosion_string = sys.stdin.readline().rstrip()
n = len(string)
m = len(explosion_string)
MIN = 0
MAX = len(explosion_string)
result = []
erased = [0] * n
for i in range(n):
    if string[i] == explosion_string[0]:
        result.append((i,0))
    else:
        if result:
            p = result[-1]
            if string[i] == explosion_string[p[1]+1]:
                result.append((i,p[1]+1))
                if p[1]+1 == m-1:
                    for j in range(m):
                        erase_index = result.pop()[0]
                        erased[erase_index] = 1
            else:
                while result:
                    result.pop()

answer = ""
for i in range(n):
    if erased[i] == 1:
        continue
    answer += string[i]

if answer:
    print(answer)
else:
    print("FAULA")