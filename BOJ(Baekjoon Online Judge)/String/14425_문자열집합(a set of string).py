#https://www.acmicpc.net/problem/14425

import sys
from collections import deque

class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.children = {}
        self.data = data

class Trie:
    def __init__(self):
        self.head = Node(None)

    def add(self, word):
        current_node = self.head
        for i in word:
            if i not in current_node.children:
                current_node.children[i] = Node(key=i)
            current_node = current_node.children[i]
        current_node.data = word

    def search(self, word):
        current_node = self.head
        for i in word:
            if i not in current_node.children:
                return False
            current_node = current_node.children[i]
        if current_node.data != None:
            return True
        else:
            return False
"""
    def start_with(self, prefix):
        current_node = self.head
        words = []
        subtrie = None

        for i in prefix:
            if i in current_node.children:
                current_node = current_node.children[i]
                subtrie = current_node
            else:
                return None
        queue = deque()
        queue.append(list(subtrie.children.values()))

        while queue:
            cur = queue.popleft()
            for node in cur:
                if node.data != None:
                    words.append(node.data)
                queue.append(list(node.children.values()))

        return words
"""
n, m = map(int,sys.stdin.readline().split())
trie = Trie()
count = 0
for i in range(n):
    trie.add(sys.stdin.readline().rstrip())
for i in range(m):
    if trie.search(sys.stdin.readline().rstrip()):
        count += 1
print(count)