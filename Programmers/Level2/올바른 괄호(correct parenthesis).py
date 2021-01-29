# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    count = 0

    for p in s:
        if p == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False

    return count == 0


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
