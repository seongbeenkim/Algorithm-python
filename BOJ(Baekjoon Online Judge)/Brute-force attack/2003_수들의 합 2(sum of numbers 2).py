#https://www.acmicpc.net/problem/2003

n,s = map(int,input().split())
a = list(map(int,input().split()))
left = right = 0
sum = a[0]
ans = 0
while left <= right and right < n:
    if sum < s:
        right += 1
        if right < n:
            sum += a[right]
    elif sum == s:
        ans += 1
        right += 1
        if right < n:
            sum += a[right]
    elif sum > s:
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = a[left]
print(ans)
