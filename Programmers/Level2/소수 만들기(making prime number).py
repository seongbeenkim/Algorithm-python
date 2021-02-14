# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    answer = 0
    nums.sort()
    n = sum(nums[-3:]) + 1
    is_prime = [True] * n

    for i in range(2, n):
        if is_prime[i] == True:
            k = i ** 2
            while k < n:
                is_prime[k] = False
                k += i

    candidate = combinations(nums, 3)

    for arr in candidate:
        if is_prime[sum(arr)] == True:
            answer += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
