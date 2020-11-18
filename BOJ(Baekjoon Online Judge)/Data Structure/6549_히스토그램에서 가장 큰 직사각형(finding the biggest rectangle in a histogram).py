#https://www.acmicpc.net/problem/6549

import sys

while True:
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 0:
        break
    n = a[0]
    a = a[1:]
    answer = 0
    s = []

    for i in range(n):
        while s and a[s[-1]] > a[i]:
            height = a[s.pop()]
            width = i
            if s:
                width = i - 1 - s[-1]
            answer = max(answer, height * width)
        s.append(i)
    while s:
        height = a[s.pop()]
        width = n
        if s:
            width = n - 1 - s[-1]
        answer = max(answer, height * width)
    print(answer)

""" n = 100,000이기 때문에 시간초과..
while True:
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 0:
        break
    n = a[0]
    answer = 0
    s = []

    for i in range(1,n+1):
        temp = []
        current_height = a[i]
        width = 2
        if s:
            previous_height = s[-1]
            if previous_height >= current_height:
                temp.append(s.pop())
                while s and s[-1] >= current_height:
                    temp.append(s.pop())
                    width += 1
                answer = max(answer, current_height * width)
                if temp:
                    for k in temp[-1::-1]:
                        s.append(k)
                s.append(current_height)
            else:
                if (len(s)+1) * previous_height < answer:
                    s.append(current_height)
                    continue
                temp.append(s.pop())
                while s and s[-1] >= previous_height:
                    temp.append(s.pop())
                    width += 1
                answer = max(answer, previous_height * width)
                if temp:
                    for k in temp[-1::-1]:
                        s.append(k)
                s.append(current_height)

        else:
            answer = max(current_height,answer)
            s.append(current_height)
    print(answer)
"""