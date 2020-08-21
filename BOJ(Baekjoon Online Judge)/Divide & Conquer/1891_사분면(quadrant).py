#https://www.acmicpc.net/problem/1891

import sys
sys.setrecursionlimit(10**4)

d, number = sys.stdin.readline().split()
x, y = map(int,sys.stdin.readline().split())
d = int(d)
dx,dy = 0,0
res = '-1'

def find_x_y(start_x,start_y,end_x,end_y,index):
    global dx,dy
    if index == len(number):
        if start_x == end_x and start_y == end_y:
            dx = start_x
            dy = start_y
        return
    mid_x = (start_x + end_x) // 2
    mid_y = (start_y + end_y) // 2

    if number[index] == '1':
        find_x_y(start_x,mid_y+1,mid_x,end_y,index+1)
    elif number[index] == '2':
        find_x_y(start_x,start_y,mid_x,mid_y,index+1)
    elif number[index] == '3':
        find_x_y(mid_x+1,start_y,end_x,mid_y,index+1)
    else:
        find_x_y(mid_x+1,mid_y+1,end_x,end_y,index+1)

find_x_y(0,0,(1<<d)-1,(1<<d)-1,0)

dx -= y
dy += x

def find_num(start_x,start_y,end_x,end_y,ans):
    global res
    if len(ans) == len(number):
        res = ans
        return
    mid_x = (start_x + end_x) // 2
    mid_y = (start_y + end_y) // 2

    if start_x <= dx <= mid_x and mid_y+1 <= dy <= end_y:
        find_num(start_x,mid_y+1,mid_x,end_y,ans+'1')
    elif start_x <= dx <= mid_x and start_y <= dy <= mid_y:
        find_num(start_x,start_y,mid_x,mid_y,ans+'2')
    elif mid_x+1 <= dx <= end_x and start_y <= dy <= mid_y:
        find_num(mid_x+1,start_y,end_x,mid_y,ans+'3')
    else:
        find_num(mid_x+1,mid_y+1,end_x,end_y,ans+'4')

if 0 <= dx <= (1<<d)-1 and 0 <= dy <= (1<<d)-1:
    find_num(0,0,(1<<d)-1,(1<<d)-1,"")

print(res)