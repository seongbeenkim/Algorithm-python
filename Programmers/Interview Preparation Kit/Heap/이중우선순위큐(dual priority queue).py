#https://www.welcomekakao.com/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    answer = []

    q = []

    for i in operations:
        op, num = i.split()
        if op == 'I':
            heapq.heappush(q, int(num))

        elif op == 'D' and q:
            if num == '1':
                maximum = max(q)
                i = q.index(maximum)
                q.index(heapq.nlargest(1,q)[0])
                q.pop(i)
                #q.pop(q.index(heapq.nlargest(1, q)[0]))
            else:
                minimum = min(q)
                i = q.index(minimum)
                q.pop(i)
                # q.pop(q.index(heapq.nsmallest(1, q)[0]))
    if q:
        answer.append(max(q))
        answer.append(min(q))
    else:
        answer.append(0)
        answer.append(0)
    return answer

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))