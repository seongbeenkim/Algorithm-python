#https://www.acmicpc.net/problem/2004

import sys

count_two = 0
count_five = 0

n, m = list(map(int,sys.stdin.readline().split()))

i = 2
while n >= i:
    count_two += n // i
    i *= 2
i = 2
while (n-m) >= i:
    count_two -= (n-m) // i
    i *= 2
i = 2
while m >= i:
    count_two -= m // i
    i *= 2

i = 5
while n >= i:
    count_five += n // i
    i *= 5
i = 5
while (n-m) >= i:
    count_five -= (n-m) // i
    i *= 5
i = 5
while m >= i:
    count_five -= m // i
    i *= 5
print(min(count_two,count_five))