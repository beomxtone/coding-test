import sys
input = sys.stdin.readline

#
# 17144번: 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144
#
# 1. 먼지를 탐색하고, 해당 먼지의 확산 정보를 구한다.
# 2. 먼지의 확산 정보가 구해지면 먼지 칸의 먼지 값을 갱신하고, 한번에 확산 정보를 갱신한다.
# 3. 공기청정기의 바람 구현
#
# @author  Asher Seo

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
graph = []
cl = 0

for i in range(r):
  graph.append(list(map(int, input().split())))
  if graph[i][0] == -1 and not cl:
    cl = i

for _ in range(t):
  # 먼지 정보
  dusts = []
  for i in range(r):
    for j in range(c):

      # 먼지가 있으면
      if graph[i][j] != 0 and graph[i][j] != -1:
        # 확산되는 먼지 정보를 담을 배열
        dust = []
        
        for k in range(4):
          nx, ny = i+dx[k], j+dy[k]
          # 방을 벗어나지 않고, 공기청정기 칸이 아니며, 확산되는 미세먼지가 0이 아닐 경우
          if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1 and graph[i][j]//5 != 0:
            dust.append((nx, ny, graph[i][j]//5))

        # (i, j) 칸에 있는 먼지는 확산된 먼지만큼 빼준다
        graph[i][j] = graph[i][j] - (graph[i][j]//5) * len(dust)
        dusts.extend(dust)

  # 확산되는 미세먼지 값들을 갱신
  for dust in dusts:
    x, y, d = dust
    graph[x][y] += d

  # 위쪽 공기청정기 바람
  graph[cl-1][0] = 0  # 정화
  
  # 왼쪽 구역
  for i in range(cl-2, -1, -1):
    graph[i+1][0] = graph[i][0]
    graph[i][0] = 0
  
  # 위쪽 구역
  for i in range(1, c):
    graph[0][i-1] = graph[0][i]
    graph[0][i] = 0

  # 오른쪽 구역
  for i in range(1, cl+1):
    graph[i-1][c-1] = graph[i][c-1]
    graph[i][c-1] = 0

  # 아래쪽 구역
  for i in range(c-2, 0, -1):
    graph[cl][i+1] = graph[cl][i]
    graph[cl][i] = 0

  # 아래쪽 공기청정기 바람
  dcl = cl+1
  graph[dcl+1][0] = 0  # 정화

  # 왼쪽 구역
  for i in range(dcl+2, r):
    graph[i-1][0] = graph[i][0]
    graph[i][0] = 0

  # 아래쪽 구역
  for i in range(1, c):
    graph[r-1][i-1] = graph[r-1][i]
    graph[r-1][i] = 0

  # 오른쪽 구역
  for i in range(r-2, dcl-1, -1):
    graph[i+1][c-1] = graph[i][c-1]
    graph[i][c-1] = 0

  # 위쪽 구역
  for i in range(c-2, 0, -1):
    graph[dcl][i+1] = graph[dcl][i]
    graph[dcl][i] = 0

# 답 계산 후 출력
ans = 0
for i in range(r):
  for j in range(c):
    if graph[i][j] != -1 and graph[i][j] != 0:
      ans += graph[i][j]

print(ans)
