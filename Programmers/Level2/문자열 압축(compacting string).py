# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)

    for i in range(1, (len(s) // 2) + 1):
        temp = ''
        count = 1
        slice = s[:i]

        for j in range(i, len(s) + i, i):
            if slice == s[j:j + i]:
                count += 1
            else:
                if count != 1:
                    temp += str(count) + slice
                else:
                    temp += slice
                slice = s[j:j + i]
                count = 1
        answer = min(answer, len(temp))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
