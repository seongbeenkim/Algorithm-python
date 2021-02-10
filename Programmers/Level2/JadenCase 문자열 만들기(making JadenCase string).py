# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    s = s.split(" ")

    for i in s:
        answer.append(i.capitalize())

    return " ".join(answer)


print(solution("3people unFollowed me"))
print(solution("for the last week"))
