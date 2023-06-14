import sys
input = sys.stdin.readline

#
# 15685번: 드래곤 커브
# https://www.acmicpc.net/problem/15685
#
# 1. 드래곤 커브의 구현은 이전 세대에서 방향값을 1씩 더해서 반대로 추가하면 된다.
# 2. 0: [0], 1: [0, 1], 2: [0, 1, 2, 1] ...
#
# @author  Asher Seo
#

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
maps = [[0]*101 for _ in range(101)]

for _ in range(n):
  # x, y: 드래곤 커브 시작 좌표, d: 방향, g: 세대
  x, y, d, g = map(int, input().split())
  maps[x][y] = 1
  dragonCurve = [d]

  for _ in range(g):
    # 다음 세대의 드래곤 커브에 반대로 추가한다.
    for i in range(len(dragonCurve)-1, -1, -1):
      # 방향값을 1씩 더하고, 4를 넘어갈 경우를 대비해 4로 나눈다.
      dragonCurve.append((dragonCurve[i] + 1) % 4)

  for i in range(len(dragonCurve)):
    x += dx[dragonCurve[i]]
    y += dy[dragonCurve[i]]
    if 0 <= x < 101 and 0 <= y < 101:
      maps[x][y] = 1

ans = 0
for i in range(100):
  for j in range(100):
    # 점을 기준으로 점, 하단, 오른쪽, 오른쪽 하단이 1이면 답 조건 달성
    if maps[i][j] == 1 and maps[i+1][j] == 1 and maps[i][j+1] == 1 and maps[i+1][j+1] == 1:
      ans += 1

print(ans)
