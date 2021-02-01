# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    result = []
    count = 0
    i = 1

    while i < len(s) - 1:
        if s[i] == '{':
            count += 1
        elif s[i] == '}':
            count -= 1
            i += 1
        elif s[i] == ',':
            i += 1
            continue

        if count == 1:
            i += 1
            arr = []
            num = ''
            while i < len(s) - 1 and s[i] != '}':
                if s[i] != ',':
                    num += s[i]
                else:
                    arr.append(int(num))
                    num = ''
                i += 1
            if num != '':
                arr.append(int(num))
            if len(arr) != 0:
                result.append(arr)

    result.sort(key=lambda x: len(x))
    numbers = dict()
    answer = []

    for arr in result:
        for num in arr:
            if num not in numbers:
                numbers[num] = 1
                answer.append(num)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
