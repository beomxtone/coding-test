import sys
input = sys.stdin.readline
from collections import deque

#
# 18258번: 큐 2
# https://www.acmicpc.net/problem/18258
#
# 1. collections library - deque 사용
#
# @author  Asher Seo
#

queue = deque()
n = int(input())
for _ in range(n):
  command = input().rstrip()
  if 'push' in command:
    queue.append(command[5:])
  elif command == 'pop':
    try:
      print(queue.popleft())
    except:
      print(-1)
  elif command == 'size':
    print(len(queue))
  elif command == 'empty':
    print(1 if len(queue) == 0 else 0)
  elif command == 'front':
    if len(queue) == 0: print(-1)
    else: print(queue[0])
  elif command == 'back':
    if len(queue) == 0: print(-1)
    else: print(queue[len(queue)-1])
  else: print('error')