import sys
input = sys.stdin.readline

#
# 10773번: 제로
# https://www.acmicpc.net/problem/10773
#
# 1. stack 자료구조를 이용해 구현 (if 0: pop, else: append)
#
# @author  Asher Seo
#

stack = []
n = int(input())

for _ in range(n):
  num = int(input())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

print(sum(stack))
