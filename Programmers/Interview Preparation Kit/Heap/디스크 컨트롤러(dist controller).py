#https://www.welcomekakao.com/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0
    h = []
    n = len(jobs)
    job = sorted(jobs)
    time = 0
    count = 0
    check = [False] * n

    while count < n:
        for i, value in enumerate(job):
            if not check[i] and value[0] <= time:
                heapq.heappush(h, (value[1], value[0]))
                check[i] = True
                break

        if len(h) > 0:
            while h:
                t, s = heapq.heappop(h)
                time += t
                answer += time - s
                count += 1
                for i, value in enumerate(job):
                    if not check[i] and value[0] <= time:
                        heapq.heappush(h, (value[1], value[0]))
                        check[i] = True
        else:
            time += 1

    return answer // n


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))