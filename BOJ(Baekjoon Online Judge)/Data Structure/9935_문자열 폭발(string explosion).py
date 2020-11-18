#https://www.acmicpc.net/problem/9935

import sys

string = sys.stdin.readline().rstrip()
explosion_string = sys.stdin.readline().rstrip()
n = len(string)
m = len(explosion_string)
result = [0] * n
fail = [0] * m
MIN = 0
MAX = len(explosion_string)

def pre_processing():
    j = 0
    for i in range(1,m):
        while j > 0 and explosion_string[i] != explosion_string[j]:
            j = fail[j-1]
        if explosion_string[i] == explosion_string[j]:
            j += 1
            fail[i] = j
        else:
            fail[i] = 0

def kmp():
    j = 0
    answer = []
    back_index = []
    for i in range(n):
        answer.append(string[i])
        while j > 0 and string[i] != explosion_string[j]:
            j = fail[j-1]
        if string[i] == explosion_string[j]:
            if j == m-1:
                for k in range(m-1):
                    answer.pop()
                    back_index.pop()
                answer.pop()
                if back_index:
                    j = back_index[-1]
                else:
                    j = 0
            else:
                j+=1
                back_index.append(j)
        else:
            back_index.append(j)
    return answer
pre_processing()
answer = kmp()
if answer:
    print(*answer, sep = "")
else:
    print("FRULA")

""" 어느 부분에서 실패하는지 정확히 모르겠다.. 다시 풀어보기
string = sys.stdin.readline().rstrip()
explosion_string = sys.stdin.readline().rstrip()
n = len(string)
m = len(explosion_string)
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
"""