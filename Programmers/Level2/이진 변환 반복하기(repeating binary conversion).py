# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(s):
    conversion_count = 0
    zero_count = 0

    while s != "1":
        conversion_count += 1
        number = s.count('1')
        zero_count += len(s) - number
        s = bin(number)[2:]

    return [conversion_count, zero_count]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
