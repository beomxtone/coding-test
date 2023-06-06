import sys
input = sys.stdin.readline

#
# 20055번: 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055
#
# 1. 컨베이어 벨트는 1차원의 스택으로 회전을 구현
#
# 2. Python은 시간초과, Pypy는 AC.
# 3. List stack 말고 deque rotate로 구현하면 python도 통과되려나?
#
# @author  Asher Seo
#

n, k = map(int, input().split())
belts = list(map(int, input().split()))
robots = [0] * n
answer = 0

while belts.count(0) < k:
  answer += 1
  # 컨베이어 벨트를 회전시킨다.
  belts.insert(0, belts[-1])
  belts.pop()

  # 로봇이 있으면
  if sum(robots):
    # 로봇 인덱스 변경
    for i in range(n-2, -1, -1):
      if robots[i]:
        robots[i+1] = 1
        robots[i] = 0
    # 로봇이 내리는 위치에 있으면 내린다.
    robots[-1] = 0
  
    # 로봇이 앞으로 한 칸 이동할 수 있는지 판단 후 이동
    for i in range(n-2, -1, -1):
      if robots[i] == 1 and robots[i+1] == 0 and belts[i+1] > 0:
        robots[i+1] = 1
        robots[i] = 0
        belts[i+1] -= 1
    # 로봇이 내리는 위치에 도달하면 내린다.
    robots[-1] = 0

  # 올리는 위치에 로봇을 올릴 수 있으면 올린다.
  if belts[0] > 0:
    robots[0] = 1
    belts[0] -= 1

print(answer)
