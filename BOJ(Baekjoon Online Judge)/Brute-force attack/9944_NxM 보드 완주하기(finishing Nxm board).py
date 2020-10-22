#https://www.acmicpc.net/problem/9944

import sys

tc = 1

while True:
    try:
        n, m = map(int,sys.stdin.readline().split())
    except:
        break

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = [[False] * m for _ in range(n)]
    a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    MAX = 901
    answer = MAX
    
    def go(x,y,dir,dist,turn_count):
        global empty_count, answer

        if dist == empty_count:
            answer = min(turn_count,answer)
            return

        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == False and a[nx][ny] == '.':
            check[nx][ny] = True
            go(nx, ny, dir, dist + 1,turn_count)
            check[nx][ny] = False
        else:
            for k in range(4):
                if k == dir:
                    continue
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == False and a[nx][ny] == '.':
                    check[nx][ny] = True
                    go(nx,ny,k,dist + 1,turn_count+1)
                    check[nx][ny] = False

    empty_count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                empty_count += 1

    if empty_count == 1:
        print("Case {}: {}".format(tc,0))
        tc+=1
        continue

    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                a[i][j] = '*'
                for dir in range(4):
                    check[i][j] = True
                    go(i,j,dir,1,1)
                    check[i][j] = False
                a[i][j] = '.'

    if answer == MAX:
        print("Case {}: {}".format(tc,-1))
    else:
        print("Case {}: {}".format(tc,answer))
    tc+=1