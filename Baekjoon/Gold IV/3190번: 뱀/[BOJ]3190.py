import sys
input = sys.stdin.readline

#
# 3190번: 뱀
# https://www.acmicpc.net/problem/3190
#
# @author  Asher Seo
#

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# n: 보드의 크기 (n*n)
n = int(input())
board = [[0]*n for _ in range(n)]
# k: 사과의 개수
k = int(input())

apples = []
for _ in range(k):
  i, j = map(int, input().split())
  apples.append((i-1, j-1))
  board[i-1][j-1] = 'A'

# L: 뱀의 방향 변환 횟수
L = int(input())
commands = []
for _ in range(L):
  x, c = input().rstrip().split()
  commands.append((int(x), c))

# 시작할 때 0으로 시작하기 위함
second = -1
# snake[0], snake[1]: 뱀의 위치 정보, snake[2]: 뱀이 보는 방향
snakes = [[0, 0, 0]]
# 부딪혔는지 여부
isHit = 0

while True:
  second += 1
  # 뱀의 머리
  snake = snakes[0]
  x, y, look = snake[0], snake[1], snake[2]
  if commands:
    command = commands[0]

  # 부딪혔으면 종료
  if isHit:
    break
  
  # 커맨드가 입력된 시간과 일치하면 방향 변경
  if command and second == command[0]:
    if command[1] == 'L':
      look += 1
      if look > 3: look = 0
    else:
      look -= 1
      if look < 0: look = 3
    commands.pop(0)
  
  # 보드를 벗어나면 종료
  if x < 0 or y < 0 or x >= n or y >= n: break

  # 사과가 있을 경우 사과를 먹는다.
  if board[x][y] == 'A':
    board[x][y] = 0
    snakes.append([snakes[-1][0], snakes[-1][1]])

  # 뱀의 꼬리에 부딛치면 종료
  for i in range(1, len(snakes)):
    if x + dx[look] == snakes[i][0] and y + dy[look] == snakes[i][1]:
      isHit = 1
      break

  # 뱀의 꼬리 갱신
  for i in range(len(snakes)-1, 0, -1):
    snakes[i][0] = snakes[i-1][0]
    snakes[i][1] = snakes[i-1][1]

  # 뱀의 머리 갱신
  snake[0], snake[1], snake[2] = x + dx[look], y + dy[look], look
  
print(second)
