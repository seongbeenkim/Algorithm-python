#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    result = 0
    k = x
    while k > 0:
        result += k % 10
        k //= 10

    if x % result == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))