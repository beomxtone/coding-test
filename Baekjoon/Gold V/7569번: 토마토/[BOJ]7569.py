import sys
input = sys.stdin.readline
from collections import deque

#
# 7569번: 토마토
# https://www.acmicpc.net/problem/7569
#
# 1. BFS 3차원 적용
# 2. 큐에 익은토마토(1) 위치 정보를 모두 넣은 후 BFS 탐색
# 3. 그래프에는 BFS의 count를 기록한다.
#
# @author  Asher Seo
#

# x, y, z가 가질 수 있는 방향 벡터
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
  while q:
    z, y, x = q.popleft()
    for i in range(6):
      nx = x + dx[i]  # nx = x-1, x+1
      ny = y + dy[i]  # ny = y-1, y+1
      nz = z + dz[i]  # nz = z-1, z+1
      # 주어진 범위를 벗어나지 않고, 이동한 방향에서의 그래프의 값이 0이면 (익지 않은 토마토면)
      if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and farm[nz][ny][nx] == 0:
        # 이동한 밭에 도달한 시간을 기록한다.
        farm[nz][ny][nx] = farm[z][y][x] + 1
        q.append((nz, ny, nx))

# m: 가로, n: 세로, h: 높이
m, n, h = map(int, input().split())
# farm: 토마토의 정보를 담은 창고
farm = [[] for _ in range(h)]
q = deque()
answer = 0

for i in range(h):
  for _ in range(n):
    # i번째 높이의 farm에 m*n의 평면 토마토 창고 저장
    farm[i].append(list(map(int, input().split())))

for i in range(h):
  for j in range(n):
    for k in range(m):
      # 해당 칸에 익은 토마토가 있을 경우
      if farm[i][j][k] == 1:
        # 큐에 위치 정보를 삽입한다.
        q.append((i, j, k))

bfs()

for i in range(h):
  for j in range(n):
    for k in range(m):
      # 익지 않은 토마토가 하나라도 있을 경우, '-1'을 출력하고 종료
      if farm[i][j][k] == 0:
        print(-1)
        exit()
      # 시작 시간이 토마토의 값인 1이기 때문에, 최종 답에서 1을 빼서 출력
      if farm[i][j][k] - 1 > answer:
        answer = farm[i][j][k] - 1

print(answer)
