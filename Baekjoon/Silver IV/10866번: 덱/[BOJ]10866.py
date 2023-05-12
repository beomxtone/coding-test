import sys
input = sys.stdin.readline
from collections import deque

#
# 10866번: 덱
# https://www.acmicpc.net/problem/10866
#
# @author  Asher Seo
#

queue = deque()
n = int(input())

for _ in range(n):
  command = input().rstrip()
  if 'push_front' in command:
    queue.appendleft(command[11:])
  elif 'push_back' in command:
    queue.append(command[10:])
  elif command == 'pop_front':
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif command == 'pop_back':
    if queue:
      print(queue.pop())
    else:
      print(-1)
  elif command == 'size':
    print(len(queue))
  elif command == 'empty':
    print(0 if queue else 1)
  elif command == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif command == 'back':
    if queue:
      print(queue[len(queue)-1])
    else:
      print(-1)
  else: print('error')