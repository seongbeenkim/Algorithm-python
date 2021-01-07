# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()

    for price in d:

        if budget - price < 0:
            break

        if budget - price >= 0:
            answer += 1
            budget -= price

    return answer


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
