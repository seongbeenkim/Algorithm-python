#https://www.acmicpc.net/problem/13505

import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
maximum = max(number)
maximum_bin_len = len(str(bin(maximum)))

class Node:

    def __init__(self,key, data = None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:

    def __init__(self):
        self.head = Node(None)

    def add(self,num):
        cur = self.head

        for i in range(len(num)):
            if num[i] not in cur.child:
                cur.child[num[i]] = Node(num[i])
            cur = cur.child[num[i]]

    def search(self,num):
        cur = self.head
        res = ''
        ans = 0

        for i in range(len(num)):
            xor = str(1-int(num[i]))
            if xor in cur.child:
                res += '1'
                cur = cur.child[xor]
            else:
                xor = str(1-int(xor))
                res += '0'
                cur = cur.child[xor]
        x = 0
        for i in range(len(res)-1,-1,-1):
            ans += int(res[i]) * 2**x
            x+=1

        return ans


ans = 0
trie = Trie()
for i in number:
    diff = 0
    bin_len = len(str(bin(i)))
    if maximum_bin_len != bin_len:
        diff = maximum_bin_len - bin_len

    trie.add((diff * "0") + str(bin(i)[2:]))

for j in number:
    diff = 0
    bin_len = len(str(bin(j)))
    if maximum_bin_len != bin_len:
        diff = maximum_bin_len - bin_len
    ans = max(ans,trie.search((diff * "0") + str(bin(j)[2:])))

print(ans)