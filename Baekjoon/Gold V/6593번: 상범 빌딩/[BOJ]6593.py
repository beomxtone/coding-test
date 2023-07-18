import sys
input = sys.stdin.readline
from collections import deque;

#
# 6593번: 상범 빌딩
# https://www.acmicpc.net/problem/6593
#
# 1. BFS로 현재 있는 층에서의 최단 경로를 구한다.
# 2. 현재 있는 칸에서 인접한 층(+1, -1)으로 갈 수 있다면, BFS로 3차원 배열을 통해 경로를 구한다.
# 3. 갈 수 있는 모든 경로를 구하고, 출구에 도달한 최단 시간을 출력한다.
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
  x, y, z = start
  visited[x][y][z] = 0
  q = deque()
  q.append(start)

  while q:
    x, y, z = q.popleft()
    for i in range(6):
      nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

      if 0<=nx<L and 0<=ny<R and 0<=nz<C:
        # 현재 visited 값이 (이전 칸 + 1) 보다 크고, 벽이 아니면
        if visited[nx][ny][nz] > visited[x][y][z] + 1 and builds[nx][ny][nz] != '#':
          # 현재 칸이 출구이면 정답 출력 후 종료
          if builds[nx][ny][nz] == 'E':
            print('Escaped in', visited[x][y][z] + 1, 'minute(s).')
            return

          # 현재 칸이 빈 칸이라면 계속 진행
          visited[nx][ny][nz] = visited[x][y][z] + 1
          q.append((nx, ny, nz))
  
  # 탈출에 실패했을 경우
  print('Trapped!')
  return


while True:
  L, R, C = map(int, input().split())

  # 0 0 0 입력되면 종료
  if L==0 and R==0 and C==0:
    break

  builds = [[list(input().rstrip()) for _ in range(R+1)] for _ in range(L)]
  visited = [[[30000]*C for _ in range(R)] for _ in range(L)]

  flag = 0
  for i in range(L):
    for j in range(R):
      for k in range(C):
        if builds[i][j][k] == 'S':
          start = (i, j, k)
          # 3중 반복문 break
          flag = 1
          break
      if flag: break
    if flag: break

  bfs()
