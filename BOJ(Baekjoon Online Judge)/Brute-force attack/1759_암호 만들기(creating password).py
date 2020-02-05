#https://www.acmicpc.net/problem/1759

import sys

sys.setrecursionlimit(10**6)

l, c = map(int,sys.stdin.readline().split())
a = sys.stdin.readline().split()
a.sort()

def go(index,password):
    if len(password) == l:
        consonant = 0
        vowel = 0
        for i in password:
            if i in "aeiou":
                vowel += 1
            else:
                consonant +=1
        if vowel >= 1 and consonant >= 2:
            sys.stdout.write(password + "\n")
            return

    if index >= c:
        return

    go(index+1, password + a[index])
    go(index+1,password)
go(0,"")
