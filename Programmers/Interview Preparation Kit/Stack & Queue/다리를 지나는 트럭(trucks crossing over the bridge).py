#https://www.welcomekakao.com/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    time = 1
    i = 0
    q = deque()
    q.append((time, truck_weights[i]))
    now = truck_weights[i]
    i += 1

    while q:
        if time - q[0][0] >= bridge_length:
            now -= q[0][1]
            q.popleft()
            answer = time

        if i < n and weight >= now + truck_weights[i]:
            now += truck_weights[i]
            q.append((time, truck_weights[i]))
            i += 1
        time += 1

    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))