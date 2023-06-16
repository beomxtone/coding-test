import sys
input = sys.stdin.readline
from collections import deque
import math

#
# 16234번: 인구 이동
# https://www.acmicpc.net/problem/16234
#
# 1. BFS로 각각 연합을 구해 인구를 이동시킨다.
# 2. BFS를 통한 인구 이동이 없을 때까지 반복
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
  q = deque()
  q.append(start)
  unions = [start]
  isUnion[start[0]][start[1]] = 1
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      # nx, ny가 나라 배열을 벗어나는지 체크
      if 0<=nx<n and 0<=ny<countriesLens[nx]:
        # 이미 연합이면 넘어감
        if isUnion[nx][ny] == 1: continue
        # l <= 인구 차이 <= r 이면 연합 추가
        if l <= abs(countries[x][y] - countries[nx][ny]) <= r:
          q.append((nx, ny))
          unions.append((nx, ny))
          isUnion[nx][ny] = 1

  # 연합이 존재하면
  if len(unions) > 1:
    # 인구수 = 연합의 인구수 / 연합을 이루고 있는 칸의 개수 (소수점 버림)
    population = 0
    for union in unions:
      population += countries[union[0]][union[1]]
    population = math.floor(population / len(unions))
    
    for union in unions:
      countries[union[0]][union[1]] = population
    return 1

  return 0


n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]
# 행의 길이
countriesLens = [len(x) for x in countries]
ans = 0

while True:
  cnt = 0
  # 연합인지 아닌지 체크
  isUnion = [[0]*x for x in countriesLens]
  
  for i in range(n):
    for j in range(countriesLens[i]):
      # 연합에 소속되어 있지 않으면 BFS 수행
      if not isUnion[i][j]:
        cnt += bfs((i, j))
  
  if cnt == 0: break
  else: ans += 1

print(ans)
