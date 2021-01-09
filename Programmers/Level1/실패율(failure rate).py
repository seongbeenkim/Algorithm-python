# https://programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter


def solution(N, stages):
    answer = []
    n = len(stages)
    count = Counter(stages)

    for i in range(1, N + 1):
        if n > 0:
            answer.append((i, count[i] / n))
            n -= count[i]
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x: -x[1])

    return [i[0] for i in answer]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
