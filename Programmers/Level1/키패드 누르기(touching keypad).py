# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    keypad = dict()

    for i in range(3):
        for j in range(3):
            keypad[str((3 * i) + (j + 1))] = (i + 1, j + 1)

    keypad['0'] = (4, 2)
    keypad['*'] = (4, 1)
    keypad['#'] = (4, 3)

    for number in numbers:
        number = str(number)
        if number in ['1', '4', '7']:
            answer += "L"
            left = number
        elif number in ['3', '6', '9']:
            answer += "R"
            right = number
        else:
            left_dist = abs(keypad[left][0] - keypad[number][0]) + abs(keypad[left][1] - keypad[number][1])
            right_dist = abs(keypad[right][0] - keypad[number][0]) + abs(keypad[right][1] - keypad[number][1])

            if left_dist == right_dist:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number
            elif left_dist > right_dist:
                answer += "R"
                right = number
            else:
                answer += "L"
                left = number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
