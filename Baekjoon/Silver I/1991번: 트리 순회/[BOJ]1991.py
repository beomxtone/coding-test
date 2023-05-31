import sys
input = sys.stdin.readline

#
# 1991번: 트리 순회
# https://www.acmicpc.net/problem/1991
#
# 1. Dictionary를 통해 트리 구현
# 2. key: Node, value: [left, right]
#
# @author  Asher Seo
#

def preorder(root):
  if root != '.':
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
  if root != '.':
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
  if root != '.':
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

# tree: key = node, value = left, right
tree = {}
n = int(input())
for _ in range(n):
  node, left, right = input().split()
  tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
