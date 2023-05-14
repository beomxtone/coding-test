import sys
input = sys.stdin.readline
from collections import deque

#
# 7576번: 토마토
# https://www.acmicpc.net/problem/7576
#
# 1. BFS를 이용하여 풀이
# 2. 익은 토마토를 모두 queue에 넣고 BFS 수행
#
# @author  Asher Seo
#

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      # farm 범위 안이면서, 다음 밭이 방문하지 않은 밭일 때
      if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] == 0:
        # 다음 밭을 방문 처리하고 queue에 삽입
        farm[nx][ny] = farm[x][y] + 1
        queue.append((nx, ny))

farm = []
queue = deque()

m, n = map(int, input().split())
for _ in range(n):
  farm.append(list(map(int, input().split())))

for i in range(n):
  for j in range(m):
    # 익은 토마토가 있으면
    if farm[i][j] == 1:
      # queue에 삽입
      queue.append((i, j))

bfs()
answer = 0

for row in farm:
  for block in row:
    # 익지 않은 토마토가 있으면 -1 출력 후 종료
    if block == 0:
      print(-1)
      exit(0)
  if answer < max(row): answer = max(row)

print(answer - 1)
