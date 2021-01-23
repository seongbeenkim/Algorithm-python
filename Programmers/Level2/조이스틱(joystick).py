# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    a = ord('A')
    z = ord('Z')
    d = [min(ord(name[i]) - a, z - ord(name[i]) + 1) for i in range(len(name))]
    i = 0

    while True:
        answer += d[i]
        d[i] = 0
        if sum(d) == 0:
            break

        left = 1
        right = 1

        while d[i - left] == 0:
            left += 1
        while d[i + right] == 0:
            right += 1

        answer += min(left, right)

        if left < right:
            i -= left
        else:
            i += right

    return answer


print(solution("JOROEN"))
print(solution("JAN"))
