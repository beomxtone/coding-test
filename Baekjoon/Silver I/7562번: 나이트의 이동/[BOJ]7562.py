import sys
input = sys.stdin.readline
from collections import deque

#
# 7562번: 나이트의 이동
# https://www.acmicpc.net/problem/7562
#
# 1. BFS - 노드마다 최단 거리를 구할 수 있다.
# 2. 각 노드는 n-1, n+1, n*2 노드에 접근할 수 있다.
#
# @author  Asher Seo
#

# 나이트가 갈 수 있는 경로
dx = [-2, -1, 2, 1, 1, 2, -1, -2]
dy = [1, 2, 1, 2, -2, -1, -2, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if chessBoard[nx][ny] > 0:
        continue
      if chessBoard[nx][ny] == 0:
        chessBoard[nx][ny] = chessBoard[x][y] + 1
        queue.append((nx, ny))

T = int(input())
for _ in range(T):
  n = int(input())
  ox, oy = map(int, input().split())
  fx, fy = map(int, input().split())
  # 출발 지점과 도착 지점이 같을 경우, 0 출력
  if ox == fx and oy == fy:
    print(0)
    continue
  chessBoard = [[0 for _ in range(n)] for _ in range(n)]

  bfs(ox, oy)
  print(chessBoard[fx][fy])
