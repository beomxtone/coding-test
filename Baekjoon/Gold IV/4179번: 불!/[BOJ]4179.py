import sys
input = sys.stdin.readline
from collections import deque

#
# 4179번: 불!
# https://www.acmicpc.net/problem/4179
#
# 1. 미로 탈출 = BFS 순회
# 2. 불은 각 초마다 4 방향으로 확산
# 3. 해당 칸마다 지훈이는 불보다 빠르거나, 불이 번지지 않은 칸에만 갈 수 있다.
# 4. 지훈이가 미로를 탈출하면 답을 출력, 탈출할 수 없으면 'IMPOSSIBLE' 출력
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  # fire 확산 정보를 담은 Queue
  while fQ:
    x, y = fQ.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if 0<=nx<r and 0<=ny<c:
        if fVisited[nx][ny] == -1 and maze[nx][ny] != '#':
          # 초기값이 -1이므로 1+1=2를 더해준다.
          fVisited[nx][ny] += fVisited[x][y] + 2
          fQ.append((nx, ny))

  # 지훈의 이동 정보를 담은 Queue
  while jQ:
    x, y = jQ.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]

      if 0<=nx<r and 0<=ny<c:
        if jVisited[nx][ny] == -1 and maze[nx][ny] != '#':
          # 불이 퍼지지 않았거나, 불이 퍼지기 전에 칸에 도달한 경우
          if fVisited[nx][ny] == -1 or fVisited[nx][ny] > jVisited[x][y] + 1:
            jVisited[nx][ny] += jVisited[x][y] + 2
            jQ.append((nx, ny))

      # 탈출 성공
      else:
        return jVisited[x][y] + 1

  # 탈출 실패
  return 'IMPOSSIBLE'


r, c = map(int, input().split())
maze = []
jVisited = [[-1]*c for _ in range(r)]
fVisited = [[-1]*c for _ in range(r)]
jQ = deque()
fQ = deque()

for i in range(r):
  maze.append(list(input().rstrip()))
  for j in range(c):
    if maze[i][j] == 'J':
      jVisited[i][j] = 0
      jQ.append((i, j))
    elif maze[i][j] == 'F':
      fVisited[i][j] = 0
      fQ.append((i, j))

print(bfs())
