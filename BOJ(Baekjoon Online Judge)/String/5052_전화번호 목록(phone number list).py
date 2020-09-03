#https://www.acmicpc.net/problem/5052

import sys

class Node:

    def __init__(self,key, data = None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:

    def __init__(self):
        self.head = Node(None)

    def add(self, num):
        cur = self.head

        for i in num:
            if i not in cur.child:
                cur.child[i] = Node(i)
            cur = cur.child[i]
        cur.data = num

    def search(self,num):
        cur = self.head

        for i in num:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        if len(cur.child) > 0:
            return True
        else:
            return False

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    number = [sys.stdin.readline().rstrip() for _ in range(n)]
    trie = Trie()
    is_consistent = True

    for i in number:
        trie.add(i)

    for i in number:
        if trie.search(i):
            is_consistent = False
            break

    if is_consistent:
        print("YES")
    else:
        print("NO")


