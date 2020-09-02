#https://www.acmicpc.net/problem/14426
# 기업 코테로 나온 문제

import sys

n, m = map(int,sys.stdin.readline().split())

string = [sys.stdin.readline().rstrip() for _ in range(n)]
pattern = [sys.stdin.readline().rstrip() for _ in range(m)]

class Node:

    def __init__(self,data = None):
        self.data = data
        self.child = {}

class Trie:

    def __init__(self):
        self.head = Node()

    def add(self,index,string,node):

        if index == len(string):
            return

        c = string[index]

        if c not in node.child:
            node.child[c] = Node(c)
        next = node.child[c]

        self.add(index+1,string,next)

    def search(self,index,string,node):

        if index == len(string):
            return True

        c = string[index]

        if c not in node.child:
            return False
        next = node.child[c]

        return self.search(index+1,string,next)

cnt = 0
trie = Trie()
for i in string:
    trie.add(0,i,trie.head)

for j in pattern:
    if trie.search(0,j,trie.head):
        cnt += 1
print(cnt)

"""
class Node:

    def __init__(self,data = None):
        self.data = data
        self.child = {}

class Trie:

    def __init__(self):
        self.head = Node()

    def add(self,string):
        cur = self.head
        for ch in string:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]


    def search(self,string):
        cur = self.head
        for ch in string:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True

cnt = 0
trie = Trie()
for i in string:
    trie.add(i)

for j in pattern:
    if trie.search(j):
        cnt += 1
print(cnt)
"""