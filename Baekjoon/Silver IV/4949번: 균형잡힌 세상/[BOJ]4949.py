import sys
input = sys.stdin.readline

#
# 4949번: 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
#
# 1. 소괄호와 대괄호를 함께 저장하는 스택을 생성한다.
# 2. 문자열은 무시하고 '(','['는 append, ')',']'는 pop을 수행한다.
# 3. pop 실행에서 오류가 발생하면 'no'를 출력한다.
# 4. pop을 실행하는 괄호와 pop의 결과물 괄호가 다를 경우, 'no'를 출력한다.
#
# @author  Asher Seo
#

while True:
  try:
    sentence = input().rstrip()
    if sentence == '.': break  # 종료조건 "."
    stack = []
    isBalance = 1
    for char in sentence:
      if char == '(' or char == '[': stack.append(char)
      elif char == ')':
        try:
          compare = stack.pop()
          if compare != '(':
            isBalance = 0
            break
        except:
          isBalance = 0
      elif char == ']':
        try:
          compare = stack.pop()
          if compare != '[':
            isBalance = 0
            break
        except:
          isBalance = 0
    if len(stack) > 0: isBalance = 0
    print('yes' if isBalance == 1 else 'no')
  except:
    break