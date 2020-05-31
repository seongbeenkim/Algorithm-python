#https://www.acmicpc.net/problem/1644

import sys

n = int(sys.stdin.readline())
nums = [i for i in range(n+1)]

for i in range(2,n+1):
    if nums[i] != 0:
        x = i**2
        while x <= n:
            nums[x] = 0
            x += i

prime = [i for i in nums[2:n+1] if i != 0]

i = 0
j = 0
sum = prime[0] if n>1 else 0
ans = 0
z = len(prime)

while i <= j and j < z:
    if sum < n:
        j+=1
        if j < z:
            sum += prime[j]
    elif sum == n:
        ans += 1
        j+=1
        if j < z:
            sum += prime[j]
    else:
        sum -= prime[i]
        i+=1
        if i<j and i<z:
            j = i
            sum = prime[i]
print(ans)