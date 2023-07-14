import sys

input = sys.stdin.readline
from collections import deque

#
# 5427번: 불
# https://www.acmicpc.net/problem/5427
#
# 1. 불과 상근이의 이동 경로를 BFS로 따로 저장한다.
# 2. 불의 이동 속도보다 상근이의 이동 시간이 느리거나 같으면, 상근이는 해당 칸으로 이동할 수 없다.
# 3. 상근이가 맵을 벗어나면 시간을 출력, 벗어나지 못하면 IMPOSSIBLE을 출력한다.
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
  # fire 확산 정보를 담은 Queue
  while fQ:
    x, y = fQ.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < h and 0 <= ny < w:
        if fVisited[nx][ny] == -1 and maps[nx][ny] != '#':
          # 초기값이 -1이므로 1+1=2를 더해준다.
          fVisited[nx][ny] += fVisited[x][y] + 2
          fQ.append((nx, ny))

  # 상근이의 이동 정보를 담은 Queue
  while sQ:
    x, y = sQ.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < h and 0 <= ny < w:
        if sVisited[nx][ny] == -1 and maps[nx][ny] != '#':
          # 불이 퍼지지 않았거나, 불이 퍼지기 전에 칸에 도달한 경우
          if fVisited[nx][ny] == -1 or fVisited[nx][ny] > sVisited[x][y] + 1:
            sVisited[nx][ny] += sVisited[x][y] + 2
            sQ.append((nx, ny))

      # 탈출 성공
      else:
        return sVisited[x][y] + 1

  # 탈출 실패
  return 'IMPOSSIBLE'


t = int(input())
for _ in range(t):
  w, h = map(int, input().split())
  maps = []
  sVisited = [[-1] * w for _ in range(h)]
  fVisited = [[-1] * w for _ in range(h)]
  sQ = deque()
  fQ = deque()

  for i in range(h):
    maps.append(list(input().rstrip()))
    for j in range(w):
      if maps[i][j] == '@':
        sVisited[i][j] = 0
        sQ.append((i, j))
      elif maps[i][j] == '*':
        fVisited[i][j] = 0
        fQ.append((i, j))

  print(bfs())
