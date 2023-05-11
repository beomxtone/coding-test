import sys
input = sys.stdin.readline

#
# 스택
# https://www.acmicpc.net/problem/13305
#
# 1. list의 append와 pop을 이용해 구현한다.
#
# @author  Asher Seo
#

stack = []
n = int(input())

for line in range(n):
  command = input().rstrip()
  if 'push' in command:
    stack.append(command[5:])
  elif command == 'pop':
    try:
      print(stack.pop())
    except:
      print(-1)
  elif command == 'size':
    print(len(stack))
  elif command == 'empty':
    print('1' if len(stack) == 0 else '0')
  elif command == 'top':
    print(stack[len(stack)-1] if len(stack) > 0 else '-1')
