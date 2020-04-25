#https://www.acmicpc.net/problem/14500

import sys

n, m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
tetromino = [[[0,1],[0,2],[0,3]],
             [[1,0],[2,0],[3,0]],
             [[0,1],[1,0],[1,1]],
             [[1,0],[2,0],[2,1]],
             [[0,-1],[0,-2],[1,-2]],
             [[-1,0],[-2,0],[-2,-1]],
             [[0,1],[0,2],[-1,2]],
             [[1,0],[2,0],[2,-1]],
             [[0,-1],[0,-2],[-1,-2]],
             [[-1,0],[-2,0],[-2,1]],
             [[0,1],[0,2],[1,2]],
             [[1,0],[1,1],[2,1]],
             [[0,-1],[1,-1],[1,-2]],
             [[1,0],[1,-1],[2,-1]],
             [[0,-1],[-1,-1],[-1,-2]],
             [[0,1],[1,1],[0,2]],
             [[1,0],[1,-1],[2,0]],
             [[0,1],[-1,1],[0,2]],
             [[1,0],[1,1],[2,0]]]

ans = 0
temp = 0
for i in range(n):
    for j in range(m):
        for k in range(19):
            temp += a[i][j]
            for x,y in tetromino[k]:
                if 0 <= i+x < n and 0 <= j+y < m:
                    temp+= a[i+x][j+y]
            if temp > ans:
                ans = temp
            temp = 0
print(ans)