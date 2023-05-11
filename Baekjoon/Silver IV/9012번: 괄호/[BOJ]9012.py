import sys
input = sys.stdin.readline

#
# 9012번: 괄호
# https://www.acmicpc.net/problem/9012
#
# 1. stack 자료구조를 이용해 구현한다.
# 2. '(' 는 append, ')' 는 pop
# 3. pop에서 오류가 나면 'NO', 끝까지 정상 작동하면 'YES'를 출력한다.
#
# @author  Asher Seo
#

n = int(input())

for _ in range(n):
  stack = []
  isVps = input().rstrip()
  isValid = 1
  for ps in isVps:
    if ps == '(':
      stack.append(0)
    else:
      try:
        stack.pop()
      except:
        isValid = 0
        break
  if len(stack) != 0: isValid = 0
  print('NO' if isValid == 0 else 'YES')