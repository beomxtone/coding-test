import sys
input = sys.stdin.readline
from collections import deque

#
# 14502번: 연구소
# https://www.acmicpc.net/problem/14502
#
# 1. 벽을 세우는 모든 경우의 수에 대해 검사
# 2. 재귀함수로 벽을 세개 세움
# 3. 벽을 세개 세웠으면 해당하는 지도에서 bfs 수행으로 결과값 갱신
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  q = deque()
  # 원본 지도 복제
  copyMap = [line[:] for line in L]
  # 바이러스를 큐에 삽입
  for i in range(n):
    for j in range(m):
      if copyMap[i][j] == 2:
        q.append((i, j))
  # BFS
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if copyMap[nx][ny] == 0:
          copyMap[nx][ny] = 2
          q.append((nx, ny))

  # count: 감염되지 않은 칸(0)의 수
  count = 0
  for i in range(n):
    for j in range(m):
      if copyMap[i][j] == 0:
        count += 1
  # answer과 현재 count값 중 큰 값을 저장
  global answer
  answer = max(answer, count)

# 벽을 세우는 재귀함수
def buildWall(count):
  # 벽을 세곳 세웠으면 bfs 함수 실행
  if count == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if L[i][j] == 0:
        L[i][j] = 1
        buildWall(count+1)
        L[i][j] = 0


# n, m: 연구소의 세로, 가로 크기
n, m = map(int, input().split())
# L: 연구소 지도를 2차원 배열로 나타낸 정보
L = []
answer = 0

for _ in range(n):
  L.append(list(map(int, input().split())))

buildWall(0)
print(answer)
