import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

#
# 17142번: 연구소 3
# https://www.acmicpc.net/problem/17142
#
# 1. 비활성 바이러스 k개중 m개를 뽑는 경우의 수만큼 브루트포스
# 2. 경우의 수마다 답을 갱신
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(q, visited):
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      
      if 0<=nx<n and 0<=ny<n:
        if visited[nx][ny] == 0 and graph[nx][ny] != 1:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))

  return visited
  

n, m = map(int, input().split())
graph = []
virus = []
flag = 1

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] == 2:
      virus.append((i, j))
    if graph[i][j] == 0:
      flag = 0

# 빈칸이 없으면 종료
if flag:
  print(0)
  exit()

ans = 10000
# 바이러스 k개 중 m개를 뽑는 경우의 수 c
for c in combinations(virus, m):
  visited = [[0]*n for _ in range(n)]
  q = deque()
  # queue에 바이러스의 위치 정보 append
  for v in c:
    q.append(v)
    visited[v[0]][v[1]] = 1

  res = bfs(q, visited)
  maxRes = 0
  
  flag = 1
  for i in range(n):
    for j in range(n):
      # 빈칸이 있으면 실패
      if graph[i][j] == 0 and res[i][j] == 0:
        flag = 0
      # 빈칸만 시간을 센다
      if graph[i][j] == 0:
        maxRes = max(maxRes, res[i][j])

  # 빈칸이 없으면 답을 갱신
  if flag:
    ans = min(ans, maxRes-1)
  
print(ans if ans != 10000 else -1)
