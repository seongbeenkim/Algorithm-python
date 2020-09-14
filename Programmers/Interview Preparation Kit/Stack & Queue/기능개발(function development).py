#https://www.welcomekakao.com/learn/courses/30/lessons/42586


import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    q = deque()
    for i in range(n):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while q:
        x = q.popleft()
        cnt = 1
        while q and x >= q[0]:
            q.popleft()
            cnt += 1
        answer.append(cnt)

    return answer


print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
