# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    temp = []

    while n > 0:
        temp += [n % 3]
        n = n // 3

    temp.reverse()

    for i, number in enumerate(temp):
        answer += (3 ** i) * number
    return answer


print(solution(45))
print(solution(125))
