import sys
input = sys.stdin.readline
from itertools import product

#
# 12100번: 2048 (Easy)
# https://www.acmicpc.net/problem/12100
#
# 1. LRUD 네 방향의 중복 순열을 구한다. (브루트포스)
# 2. 1에서 구한 1024가지의 순열에 따라 게임을 구현한다.
#
# @author  Asher Seo
#

def move(board, command):
  
  if command == 'L':
    for i in range(n):
      for j in range(1, n):
        # 맨 끝까지 수가 있는지 여부
        flag = 1
        # 왼쪽 칸 중 수가 있는 곳을 찾는다.
        for k in range(j-1, -1, -1):
          if board[i][k] != 0:
            # 왼쪽의 가장 가까운 수가 현재 칸의 값과 같으면 합친다.
            if board[i][k] == board[i][j]:
              board[i][k] *= 2
              # 중복해서 더해지는 것을 방지하기 위해 1을 더해준다.
              board[i][k] += 1
              board[i][j] = 0
            # 다르면 그 수의 왼쪽으로 이동한다.
            elif k != j-1:
              board[i][k+1] = board[i][j]
              board[i][j] = 0
            flag = 0
            break
        # 끝까지 수가 없으면 맨 끝으로 현재 수를 이동시킨다.
        if flag:
          board[i][0] = board[i][j]
          board[i][j] = 0

  if command == 'R':
    for i in range(n):
      for j in range(n-2, -1, -1):
        flag = 1
        for k in range(j+1, n):
          if board[i][k] != 0:
            if board[i][k] == board[i][j]:
              board[i][k] *= 2
              board[i][k] += 1
              board[i][j] = 0
            
            elif k != j+1:
              board[i][k-1] = board[i][j]
              board[i][j] = 0
            flag = 0
            break
          
        if flag:
          board[i][n-1] = board[i][j]
          board[i][j] = 0

  if command == 'U':
    for i in range(1, n):
      for j in range(n):
        flag = 1
        for k in range(i-1, -1, -1):
          if board[k][j] != 0:
            if board[k][j] == board[i][j]:
              board[k][j] *= 2
              board[k][j] += 1
              board[i][j] = 0
            
            elif k != i-1:
              board[k+1][j] = board[i][j]
              board[i][j] = 0
            flag = 0
            break
          
        if flag:
          board[0][j] = board[i][j]
          board[i][j] = 0

  if command == 'D':
    for i in range(n-2, -1, -1):
      for j in range(n):
        flag = 1
        for k in range(i+1, n):
          if board[k][j] != 0:
            if board[k][j] == board[i][j]:
              board[k][j] *= 2
              board[k][j] += 1
              board[i][j] = 0
            
            elif k != i+1:
              board[k-1][j] = board[i][j]
              board[i][j] = 0
            flag = 0
            break
          
        if flag:
          board[n-1][j] = board[i][j]
          board[i][j] = 0

  # 합쳐진 것들에 1을 더해줬던 것을 제거
  for i in range(n):
    for j in range(n):
      if board[i][j] % 2 == 1:
        board[i][j] -= 1
  

n = int(input())
rawBoard = [list(map(int, input().split())) for _ in range(n)]
commandCase = ['L', 'R', 'U', 'D']
answer = 0

for commands in product(commandCase, repeat=5):
  board = [x[:] for x in rawBoard]

  for command in commands:
    move(board, command)

  answer = max(answer, max(map(max, board)))

print(answer)
