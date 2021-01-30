# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    m = bin(n)[2:].count('1')

    for i in range(n + 1, 1000000):
        if bin(i)[2:].count('1') == m:
            return i


print(solution(78))
print(solution(15))
