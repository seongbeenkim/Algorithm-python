# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    strings.sort()
    letters = set()

    for string in strings:
        letters.add(string[n])
    letters = sorted(list(letters))

    for letter in letters:
        for string in strings:
            if string[n] == letter:
                answer.append(string)
    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))

#
# def solution(strings, n):
#     strings.sort()
#     return sorted(strings, key = lambda x: x[n])
#
