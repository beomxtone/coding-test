import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#
# 2263번: 트리의 순회
# https://www.acmicpc.net/problem/2263
#
# 1. 포스트오더의 마지막 값 = root
# 2. root값은 인오더의 중간 값 => root의 왼쪽, 오른쪽 값들은 각각 왼쪽, 오른쪽 서브트리
#
# @author  Asher Seo
#

def preorder(x1, y1, x2, y2):
  if x1 > y1 or x2 > y2: return

  root = postorder[y2]
  left = nodes[root] - x1 - 1
  right = y1 - nodes[root]

  print(root, end=" ")
  preorder(x1, x1+left, x2, x2+left)
  preorder(y1-right+1, y1, y2-right, y2-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodes = [0] * (n+1)
for i in range(n):
  nodes[inorder[i]] = i

preorder(0, n-1, 0, n-1)
