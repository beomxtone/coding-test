import sys
input = sys.stdin.readline
from collections import deque

#
# 13460번: 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
#
# 1. BFS로 빨간 구슬이 구멍에 빠지거나, 10번의 횟수까지 반복한다.
# 2. 4방향 중 파란 구슬이 구멍에 빠진 경우는 무시하고 다른 방법을 진행한다.
# 3. 각각 도착한 칸에 다른 색의 구슬이 있으면 움직인 칸이 많은 구슬의 이동 횟수를 한번 빼준다.
#
# @author  Asher Seo

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, bx, by):
  q = deque()
  q.append((rx, ry, bx, by))
  visited = [(rx, ry, bx, by)]
  cnt = 0

  while q:
    for _ in range(len(q)):
      rx, ry, bx, by = q.popleft()
      
      if cnt > 10:
        return -1
      
      if board[rx][ry] == 'O':
        return cnt
  
      for i in range(4):
        # 빨간 구슬의 이동 방향
        nrx, nry = rx+dx[i], ry+dy[i]
  
        while board[nrx][nry] != '#':
          # 구멍에 도착하면 break
          if board[nrx][nry] == 'O':
            break
          nrx += dx[i]
          nry += dy[i]
        # 도착 지점이 벽이면 1칸 후퇴
        if board[nrx][nry] == '#':
          nrx -= dx[i]
          nry -= dy[i]
  
        # 파란 구슬의 이동 방향
        nbx, nby = bx+dx[i], by+dy[i]
  
        while board[nbx][nby] != '#':
          if board[nbx][nby] == 'O':
            break
          nbx += dx[i]
          nby += dy[i]
  
        if board[nbx][nby] == '#':
          nbx -= dx[i]
          nby -= dy[i]
  
        # 파란 구슬이 구멍에 도착하는 경우는 무시
        if board[nbx][nby] == 'O':
          continue
  
        # 두 구슬이 겹치는 경우, 이동한 칸이 많은 구슬을 한칸 후퇴
        if nrx == nbx and nry == nby:
          if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
  
        # 방문한 적 없는 경우이면 다음 반복 실행
        if (nrx, nry, nbx, nby) not in visited:
          q.append((nrx, nry, nbx, nby))
          visited.append((nrx, nry, nbx, nby))
  
    cnt += 1
  # 더 이상 움직일 칸이 없으면 -1 리턴
  return -1


n, m = map(int, input().split())
rx, ry, bx, by = 0, 0, 0, 0
board = []

for i in range(n):
  board.append(list(input().rstrip()))
  for j in range(m):
    if board[i][j] == 'R':
      rx, ry = i, j
    elif board[i][j] == 'B':
      bx, by = i, j

print(bfs(rx, ry, bx, by))
