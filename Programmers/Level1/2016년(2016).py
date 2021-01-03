# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0

    for i in range(a - 1):
        count += month[i]

    count += b
    return day[count % len(day) - 1]


print(solution(5, 24))
