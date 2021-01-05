# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    lower_a = 97
    upper_a = 65

    for ch in s:
        if "a" <= ch <= "z":
            answer += chr(((ord(ch) + n) % lower_a) % 26 + lower_a)
        elif "A" <= ch <= "Z":
            answer += chr(((ord(ch) + n) % upper_a) % 26 + upper_a)
        else:
            answer += ' '
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))