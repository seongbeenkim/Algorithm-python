# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    count_p = s.lower().count('p')
    count_y = s.lower().count('y')

    if count_p != count_y:
        return False

    return True


print(solution("pPoooyY"))
print(solution("Pyy"))
