#https://www.acmicpc.net/problem/1991

import sys
sys.setrecursionlimit(10**5)
class Node():
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

def pre_order(i): # Parent - Left - Right
    if i == -1:
        return
    print(chr(i+A), end = "")
    pre_order(tree[i].left)
    pre_order(tree[i].right)

def in_order(i): # Left - Parent - Right
    if i == -1:
        return
    in_order(tree[i].left)
    print(chr(i+A), end="")
    in_order(tree[i].right)

def post_order(i): # Left - Right - Parent
    if i == -1:
        return
    post_order(tree[i].left)
    post_order(tree[i].right)
    print(chr(i+A), end="")

n = int(sys.stdin.readline())
tree = [Node() for _ in range(26)] # A ~ Z : 26

A = ord("A")
null = ord(".")

for i in range(n):
    data, left, right = map(ord,sys.stdin.readline().split())  # A ~ Z (65 ~ 90)

    if left == null:
        left = -1
    else:
        left -= A

    if right == null:
        right = -1
    else:
        right -= A
    data -= A  # A ~ Z (65 ~ 90) => (0 ~ 25) for tree[]

    tree[data].left = left
    tree[data].right = right

pre_order(0)
print()
in_order(0)
print()
post_order(0)