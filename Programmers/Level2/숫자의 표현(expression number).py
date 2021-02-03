# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        total = i
        j = i + 1

        while total < n:
            total += j
            j += 1

        if total == n:
            answer += 1

    return answer


print(solution(15))
