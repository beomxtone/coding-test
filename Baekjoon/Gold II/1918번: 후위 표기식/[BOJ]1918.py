import sys
input = sys.stdin.readline

#
# 1918번: 후위 표기식
# https://www.acmicpc.net/problem/1918
#
# 1. 입력받은 값이 A, B, C 등의 문자이면 그대로 출력한다.
# 2. 연산자나 괄호면 조건에 맞게 stack에 push, pop 한다.
# 3. 최종 결과를 출력한다.
#
# @author  Asher Seo
#

def prefix(seq):
  stack = []
  priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
  ans = ''

  for s in seq:
    # 닫는 괄호이면 (가 나올 때까지 stack에서 pop
    if s == ')':
      while stack:
        item = stack.pop()
        if item == '(': break
        ans += item

    # 연산자가 아니면 그대로 출력
    elif s not in priority:
      ans += s

    # 연산자일 경우
    else:
      while stack and s != '(':
        # 현재 값의 우선순위가 스택 맨 위의 우선순위보다 높지 않으면 뽑아낸다.
        if priority[s] > priority[stack[-1]]: break
        ans += stack.pop()
      stack.append(s)

  # 스택에 남은 연산자를 모두 뽑아낸다.
  while stack:
    item = stack.pop()
    if item != '(': ans += item
  
  return ans


seq = list(input().rstrip())
print(prefix(seq))
