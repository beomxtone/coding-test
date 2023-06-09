import sys
input = sys.stdin.readline
from collections import deque

#
# 14891번: 톱니바퀴
# https://www.acmicpc.net/problem/14891
#
# 1. 기준 기어를 기준으로 왼쪽, 오른쪽의 기어들을 모두 조건에 맞게 돌린다.
# 2. 1은 맨 끝 기어가 나오거나, 각 방향의 기어가 돌지 않을 때까지 재귀함수를 통해 구현한다.
# 3. 기준 기어를 돌린다.
# 4. 최종 결과물 값을 출력한다.
#
# @author  Asher Seo
#

def rightRotate(cnt, dir):
  if cnt > 2:
    return

  if gears[cnt][2] != gears[cnt+1][6]:
    rightRotate(cnt+1, -1*dir)
    q = deque(gears[cnt+1])
    q.rotate(dir)
    gears[cnt+1] = q

def leftRotate(cnt, dir):
  if cnt < 1:
    return

  if gears[cnt][6] != gears[cnt-1][2]:
    leftRotate(cnt-1, -1*dir)
    q = deque(gears[cnt-1])
    q.rotate(dir)
    gears[cnt-1] = q


gears = [list(map(int, list(input().rstrip()))) for _ in range(4)]
k = int(input())
commands = [list(map(int, input().split())) for _ in range(k)]

for cmd in commands:
  # dir: 1) 시계방향, -1) 반시계방향
  num, dir = cmd[0]-1, cmd[1]

  rightRotate(num, -1*dir)
  leftRotate(num, -1*dir)

  # 기준 기어를 돌린다.
  q = deque(gears[num])
  q.rotate(dir)
  gears[num] = q

# 정답 계산
ans = 0
for i in range(4):
  if gears[i][0] == 1:
    ans += 2**i
print(ans)
