#https://www.welcomekakao.com/learn/courses/30/lessons/42587

from collections import deque
import itertools

def solution(priorities, location):
    answer = 0
    q = deque()
    target = (location,priorities[location])
    cnt = 0

    for idx, value in enumerate(priorities):
        q.append((idx,value))

    while q:
        i, v = q.popleft()
        is_biggest = True
        if q:
            slice = itertools.islice(q,0,len(q))
            for ci, cv in slice:
                if v < cv:
                    is_biggest = False
                    break

        if is_biggest:
            cnt += 1
            if i == target[0] and v == target[1]:
                answer = cnt
                break

        else:
            q.append((i,v))
    return answer

#print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))