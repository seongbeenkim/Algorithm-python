#https://www.acmicpc.net/problem/12970

import sys

n, k = map(int,sys.stdin.readline().split())

if k == 0:
    print((n-1)*"B" + "A")

elif k == 1:
    print((n-2)*"B" + "AB")

elif k == 2:
    if n >= 3:
        print((n-3)*"B" + "ABB")
    else:
        print(-1)
else:
    string = ["B"] * n
    cnt = 0
    ans = []
    for i in range(1,n+1):
        cnt += n - i - len(ans)
        if cnt < k:
            ans.append(i)
        elif cnt == k:
            ans.append(i)
            break
        else:
            cnt -= n - i - len(ans)

    if cnt != k:
        print(-1)
    else:
        for i in ans:
            string[i-1] = "A"
        print(*string, sep="")