# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    n = len(s)
    middle = n // 2
    if n % 2 != 0:
        return s[middle]
    else:
        return s[middle - 1] + s[middle]


print(solution("abcde"))
print(solution("qwer"))
