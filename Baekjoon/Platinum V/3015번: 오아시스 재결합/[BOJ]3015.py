import sys
input = sys.stdin.readline

#
# 3015번: 오아시스 재결합
# https://www.acmicpc.net/problem/3015
#
# 1. 스택을 이용하여 풀이
# 2. 키가 작아지면 스택에 넣고, 같거나 커지면 해당 사람을 기준으로 마주볼 수 있는 쌍을 구한다.
# 3. 해당 사람의 키와 같은 범위까지 pop, 마지막까지 반복 후 쌍의 수를 출력
# 4. 스택에는 [value, count] 의 구조로 삽입
#
# @author  Asher Seo
#

n = int(input())
heights = [int(input()) for _ in range(n)]
stk = []
ans = 0

for h in heights:
  # 스택 top이 현재 사람보다 작은 사람이면 pop
  while stk and stk[-1][0] < h:
    ans += stk.pop()[1]

  # 스택이 비었으면 사람 추가
  if not stk:
    stk.append((h, 1))

  # 스택의 top과 키가 같으면
  elif stk[-1][0] == h:
    top = stk.pop()
    ans += top[1]

    # 스택이 있다 = top보다 큰 사람(B)이 왼쪽에 있다
    # = B와 현재 사람 사이에 현재 사람보다 큰 사람이 없으므로 B와 현재 사람은 서로 볼 수 있다.
    if stk: ans += 1
    # 현재 사람과 같은 키의 서로 볼 수 있는 사람의 수: top[1]+1
    stk.append((h, top[1]+1))

  # 스택의 top보다 키가 작으면
  elif stk[-1][0] > h:
    ans += 1
    stk.append((h, 1))

print(ans)
