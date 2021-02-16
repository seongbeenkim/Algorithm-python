# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(records):
    id = dict()
    users = []
    status = []
    answer = []
    enter = "님이 들어왔습니다."
    leave = "님이 나갔습니다."

    for record in records:
        arr = record.split()

        if len(arr) == 3:
            id[arr[1]] = arr[2]

        if arr[0] == "Enter":
            users.append(arr[1])
            status.append(enter)
        elif arr[0] == "Leave":
            users.append(arr[1])
            status.append(leave)
        else:
            id[arr[1]] = arr[2]

    for i in range(len(users)):
        answer.append(id[users[i]] + status[i])

    return answer


print(solution(
    ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"]))
