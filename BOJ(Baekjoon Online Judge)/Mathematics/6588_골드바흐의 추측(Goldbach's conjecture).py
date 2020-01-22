#https://www.acmicpc.net/problem/6588

import sys

max = 1000000
is_prime = [True] * (max + 1)
prime = []
for i in range(2,max+1):
    if is_prime[i] == True:
        prime.append(i)
        j = 2*i
        while j <= max:
            is_prime[j] = False
            j += i
del prime[0]

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    a = 0
    b = a
    final_a = -1
    final_b = -1
    while a < len(prime):
        if (prime[a] + prime[b]) < num and a <= b:
            if final_a == -1:
                if b < (len(prime) - 1):
                    b += 1
                else:
                    a += 1
                    b = a + 1
            else:
                if b > 0:
                    b -= 1
                else:
                    a += 1
                    b = a + 1
        elif (prime[a] + prime[b]) > num:
            a += 1
            if final_b == -1:
                b = a + 1
            else:
                b = final_b - 1
        else:
            if final_a == -1:
                final_a = a
            if final_b < b:
                final_b = b
            break
    print("{0} = {1} + {2}".format(num,prime[final_a],prime[final_b]))