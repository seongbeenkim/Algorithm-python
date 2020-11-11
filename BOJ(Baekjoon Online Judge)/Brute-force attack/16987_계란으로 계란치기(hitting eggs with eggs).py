#https://www.acmicpc.net/problem/16987

import sys

n = int(sys.stdin.readline())
eggs = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

answer = 0

def dfs(idx,res,n):
    global answer

    if idx == n:
        answer = max(res,answer)
        return

    if eggs[idx][0] <= 0: # 손에 든 계란이 깨졌는지 확인
        dfs(idx+1,res,n)
        return

    is_all_broken = True
    for i in range(n): # 손에 들지 않은 계란들이 모두 깨졌는지 확인
        if i == idx:
            continue
        if eggs[i][0] > 0:
            is_all_broken = False
            break
    if is_all_broken:
        dfs(n,res,n)

    for i in range(n): # 깨지지 않은 계란 하나씩 치는 과정
        if i == idx:
            continue
        if eggs[i][0] <= 0:
            continue
        first_egg_damage = eggs[idx][0] - eggs[i][1]
        second_egg_damage = eggs[i][0] - eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        if first_egg_damage <= 0 and second_egg_damage <= 0:
            dfs(idx + 1, res + 2, n)
        elif first_egg_damage <= 0 and second_egg_damage > 0:
            dfs(idx + 1, res + 1, n)
        elif first_egg_damage > 0 and second_egg_damage > 0:
            dfs(idx + 1, res, n)
        elif first_egg_damage > 0 and second_egg_damage <= 0:
            dfs(idx + 1, res + 1, n)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]
dfs(0,0,n)
print(answer)