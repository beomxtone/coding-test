import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

#
# 17135번: 캐슬 디펜스
# https://www.acmicpc.net/problem/17135
#
# 1. M은 최대 15이므로, 궁수를 배치할 최대 경우의 수는 15C3 = 455가지
# 2. 방어는 적이 내려오는 횟수 = 최대 N번 이므로 455*15 = 최대 6825번 반복
# 3. 궁수는 세 명이므로 6825*3 = 최대 20475번 반복
# 4. 궁수의 사정거리 D = 최대 10, 왼쪽부터 탐색해서 가장 가까운 적을 쏘면 break
#
# @author  Asher Seo
#

# 화살이 아래로 가는 경우는 없고, 왼쪽 부터 쏜다
dx = [0, -1, 0]
dy = [-1, 0, 1]

def arrow(archer, board):
  visited = [[0]*m for _ in range(len(board))]
  q = deque()
  q.append((len(board), archer, 0))

  while q:
    x, y, dist = q.popleft()
    dist += 1
    
    for k in range(3):
      nx = x + dx[k]
      ny = y + dy[k]

      if nx < 0 or ny < 0 or nx >= len(board) or ny >= m:
        continue

      if visited[nx][ny]: continue

      # 적을 잡으면 return
      if board[nx][ny] == 1:
        return (nx, ny, dist)

      q.append((nx, ny, dist))
      visited[nx][ny] = 1

  # 잡은 적이 없으면 0을 return
  return (0, 0, 0)


n, m, d = map(int, input().split())
board = []
count = 0  # 적이 있는 마지막 행
ans = 0

for i in range(n):
  board.append(list(map(int, input().split())))
  # 디펜스를 몇 번 반복할지 체크
  if count == 0 and sum(board[i]) > 0:
    count = n-i

# 궁수를 뽑는 경우의 수
for archers in combinations(range(m), 3):
  res, cnt = 0, count
  copiedBoard = [arr[:] for arr in board]

  # 마지막 적이 성에 도달할 때까지
  while cnt != 0:
    # 궁수가 잡은 적들의 위치 (같은 적이 여러 번 공격 당할 수 있다.)
    enemies = []
    
    # 궁수마다 체크
    for archer in archers:
      x, y, isHit = arrow(archer, copiedBoard)
      # 사거리 내에 잡은 적이 있으면
      if isHit and isHit <= d:
        if (x, y) not in enemies:
          enemies.append((x, y))

    # 잡은 적들의 위치 정보 갱신
    for enemy in enemies:
      copiedBoard[enemy[0]][enemy[1]] = 0
    res += len(enemies)

    # 한 칸 땡김
    copiedBoard.pop()
    cnt -= 1

  ans = max(ans, res)

print(ans)
