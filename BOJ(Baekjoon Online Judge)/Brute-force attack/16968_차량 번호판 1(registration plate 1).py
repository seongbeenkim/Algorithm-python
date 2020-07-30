#https://www.acmicpc.net/problem/16968

import sys


a = list(sys.stdin.readline().rstrip())
ans = 0

def go(index,candi):
    cnt = 0

    if len(candi) == len(a):
        return 1
    if index >= len(a):
        return 0

    if a[index] == "c":
        for i in range(ord('a'),ord('z')+1):
            if len(candi) == 0:
                cnt += go(index+1,candi+[chr(i)])
            else:
                if candi[-1] != chr(i):
                    cnt += go(index + 1, candi + [chr(i)])
    else:
        for i in range(0,10):
            if len(candi) == 0:
                cnt += go(index+1,candi+[str(i)])
            else:
                if candi[-1] != str(i):
                    cnt += go(index + 1, candi + [str(i)])

    return cnt
ans += go(0,[])

print(ans)