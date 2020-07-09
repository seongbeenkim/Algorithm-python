#https://www.acmicpc.net/problem/10820

import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    lower = 0
    upper = 0
    number = 0
    blank = 0
    for i in s:
        if i == " ":
            blank += 1
        elif ord('a') <= ord(i) <= ord('z'):
            lower += 1
        elif ord('A') <= ord(i) <= ord('Z'):
            upper += 1
        else:
            number += 1

    print(lower,upper,number,blank)