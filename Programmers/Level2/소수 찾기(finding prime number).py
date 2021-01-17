# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


#
# def solution(numbers):
#     n = len(numbers)
#
#     def go(num, m):
#         result = []
#
#         if len(num) == m:
#             return [int(num)]
#
#         for i in range(n):
#             if check[i]:
#                 continue
#             check[i] = True
#             result += go(num + numbers[i], m)
#             check[i] = False
#
#         return result
#
#     temp = []
#
#     for i in range(n):
#         check = [False] * n
#         temp += go('', i + 1)
#
#     temp = list(set(temp))
#     maximum = max(temp) + 1
#     check = [False] * maximum
#     answer = 0
#
#     for i in range(2, maximum):
#         if check[i] == False and i in temp:
#             check[i] = True
#             answer += 1
#
#         k = i * i
#
#         while k < maximum:
#             check[k] = True
#             k += i
#
#     return answer

print(solution("17"))
print(solution("011"))
