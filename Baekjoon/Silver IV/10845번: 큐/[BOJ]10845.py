import sys
input = sys.stdin.readline

#
# 10845번: 큐
# https://www.acmicpc.net/problem/10845
#
# 1. deque 사용하기
#
# @author  Asher Seo
#

from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
  inputs = input().split()
  cmd = inputs[0]
  
  if 'push' in cmd:
    queue.append(inputs[1])

  if cmd == 'pop':
    if not queue:
      print(-1)
      continue
    print(queue.popleft())

  if cmd == 'size':
    print(len(queue))

  if cmd == 'empty':
    print(0 if queue else 1)

  if cmd == 'front':
    print(-1 if not queue else queue[0])

  if cmd == 'back':
    print(-1 if not queue else queue[-1])
