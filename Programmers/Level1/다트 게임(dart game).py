# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = []
    number = ''

    for ch in dartResult:
        if ch.isnumeric():
            number += ch
            continue

        if ch == "S":
            answer.append(int(number) ** 1)
        elif ch == "D":
            answer.append(int(number) ** 2)
        elif ch == "T":
            answer.append(int(number) ** 3)
        elif ch == "*":
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif ch == "#":
            answer[-1] *= -1
        number = ''

    return sum(answer)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
