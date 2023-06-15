import sys
input = sys.stdin.readline

#
# 5373번: 큐빙
# https://www.acmicpc.net/problem/5373
#
# 1. 윗면: w, 아랫면: y, 앞면: r, 뒷면: o, 왼쪽면: g, 오른쪽면: b
#
# @author  Asher Seo
#

# arr: 3*3 array, dir: +, -
def rotate(arr, dir):
  temp = arr[0][:]

  # 시계 방향으로 회전
  if dir == '+':
    arr[0][0] = arr[2][0]
    arr[0][1] = arr[1][0]
    arr[0][2] = temp[0]

    arr[2][0] = arr[2][2]
    arr[1][0] = arr[2][1]

    arr[2][2] = temp[2]
    arr[2][1] = arr[1][2]
    arr[1][2] = temp[1]

  # 반시계 방향으로 회전
  else:
    arr[0][0] = temp[2]
    arr[0][1] = arr[1][2]
    arr[0][2] = arr[2][2]

    arr[1][2] = arr[2][1]
    arr[2][2] = arr[2][0]

    arr[2][1] = arr[1][0]
    arr[2][0] = temp[0]
    arr[1][0] = temp[1]


TC = int(input())
for _ in range(TC):
  n = int(input())
  # U: 윗면, D: 아랫면, F: 앞면, B: 뒷면, L: 왼쪽면, R: 오른쪽면 / +: 시계방향, -: 반시계방향
  commands = list(input().split())
  # cube[a][b][c]  a: 면, b: 행, c: 한칸
  cube = [
    [['w' for _ in range(3)] for _ in range(3)],
    [['y' for _ in range(3)] for _ in range(3)],
    [['r' for _ in range(3)] for _ in range(3)],
    [['o' for _ in range(3)] for _ in range(3)],
    [['g' for _ in range(3)] for _ in range(3)],
    [['b' for _ in range(3)] for _ in range(3)]
  ]

  # 불필요한 횟수 제거
  i = 0
  while i < len(commands)-1:
    if len(commands) < 2: break
    if commands[i][0] == commands[i+1][0] and commands[i][1] != commands[i+1][1]:
      del commands[i]
      del commands[i]
      i = 0
    else:
      i += 1

  for command in commands:
    roll, dir = command[0], command[1]
    # 의미가 없는 경우 패스
    if roll == 'P': continue
    
    # 윗면을 돌림
    if roll == 'U':
      temp = cube[2][0][:]
      rotate(cube[0], dir)
      # 앞면 -> 왼쪽면, 왼쪽면 -> 뒷면, 뒷면 -> 오른쪽면, 오른쪽면 -> 앞면
      if dir == '+':
        cube[2][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = cube[4][0]
        cube[4][0] = temp
      # 앞면 -> 오른쪽면, 오른쪽면 -> 뒷면, 뒷면 -> 왼쪽면, 왼쪽면 -> 앞면
      else:
        cube[2][0] = cube[4][0]
        cube[4][0] = cube[3][0]
        cube[3][0] = cube[5][0]
        cube[5][0] = temp

    # 아랫면을 돌림
    elif roll == 'D':
      temp = cube[2][2][:]
      rotate(cube[1], dir)
      
      if dir == '+':
        cube[2][2] = cube[4][2]
        cube[4][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = temp
        
      else:
        cube[2][2] = cube[5][2]
        cube[5][2] = cube[3][2]
        cube[3][2] = cube[4][2]
        cube[4][2] = temp

    # 앞면을 돌림
    elif roll == 'F':
      temp = cube[0][2][:]
      rotate(cube[2], dir)
      
      if dir == '+':
        cube[0][2][0] = cube[4][2][2]
        cube[0][2][1] = cube[4][1][2]
        cube[0][2][2] = cube[4][0][2]

        cube[4][0][2] = cube[1][0][0]
        cube[4][1][2] = cube[1][0][1]
        cube[4][2][2] = cube[1][0][2]

        cube[1][0][0] = cube[5][2][0]
        cube[1][0][1] = cube[5][1][0]
        cube[1][0][2] = cube[5][0][0]

        cube[5][0][0] = temp[0]
        cube[5][1][0] = temp[1]
        cube[5][2][0] = temp[2]

      else:
        cube[0][2][0] = cube[5][0][0]
        cube[0][2][1] = cube[5][1][0]
        cube[0][2][2] = cube[5][2][0]

        cube[5][0][0] = cube[1][0][2]
        cube[5][1][0] = cube[1][0][1]
        cube[5][2][0] = cube[1][0][0]

        cube[1][0][0] = cube[4][0][2]
        cube[1][0][1] = cube[4][1][2]
        cube[1][0][2] = cube[4][2][2]

        cube[4][0][2] = temp[2]
        cube[4][1][2] = temp[1]
        cube[4][2][2] = temp[0]

    # 뒷면을 돌림
    elif roll == 'B':
      temp = cube[0][0][:]
      rotate(cube[3], dir)

      if dir == '+':
        cube[0][0][0] = cube[5][0][2]
        cube[0][0][1] = cube[5][1][2]
        cube[0][0][2] = cube[5][2][2]

        cube[5][0][2] = cube[1][2][2]
        cube[5][1][2] = cube[1][2][1]
        cube[5][2][2] = cube[1][2][0]

        cube[1][2][0] = cube[4][0][0]
        cube[1][2][1] = cube[4][1][0]
        cube[1][2][2] = cube[4][2][0]

        cube[4][0][0] = temp[2]
        cube[4][1][0] = temp[1]
        cube[4][2][0] = temp[0]

      else:
        cube[0][0][0] = cube[4][2][0]
        cube[0][0][1] = cube[4][1][0]
        cube[0][0][2] = cube[4][0][0]

        cube[4][0][0] = cube[1][2][0]
        cube[4][1][0] = cube[1][2][1]
        cube[4][2][0] = cube[1][2][2]

        cube[1][2][0] = cube[5][2][2]
        cube[1][2][1] = cube[5][1][2]
        cube[1][2][2] = cube[5][0][2]

        cube[5][0][2] = temp[0]
        cube[5][1][2] = temp[1]
        cube[5][2][2] = temp[2]

    # 왼쪽면을 돌림
    elif roll == 'L':
      temp = [x[0] for x in cube[0]][:]
      rotate(cube[4], dir)

      if dir == '+':
        cube[0][0][0] = cube[3][2][2]
        cube[0][1][0] = cube[3][1][2]
        cube[0][2][0] = cube[3][0][2]

        cube[3][0][2] = cube[1][2][0]
        cube[3][1][2] = cube[1][1][0]
        cube[3][2][2] = cube[1][0][0]

        cube[1][0][0] = cube[2][0][0]
        cube[1][1][0] = cube[2][1][0]
        cube[1][2][0] = cube[2][2][0]

        cube[2][0][0] = temp[0]
        cube[2][1][0] = temp[1]
        cube[2][2][0] = temp[2]

      else:
        cube[0][0][0] = cube[2][0][0]
        cube[0][1][0] = cube[2][1][0]
        cube[0][2][0] = cube[2][2][0]

        cube[2][0][0] = cube[1][0][0]
        cube[2][1][0] = cube[1][1][0]
        cube[2][2][0] = cube[1][2][0]

        cube[1][0][0] = cube[3][2][2]
        cube[1][1][0] = cube[3][1][2]
        cube[1][2][0] = cube[3][0][2]

        cube[3][0][2] = temp[2]
        cube[3][1][2] = temp[1]
        cube[3][2][2] = temp[0]

    # 오른쪽면을 돌림
    else:
      temp = [x[2] for x in cube[0]][:]
      rotate(cube[5], dir)

      if dir == '+':
        cube[0][0][2] = cube[2][0][2]
        cube[0][1][2] = cube[2][1][2]
        cube[0][2][2] = cube[2][2][2]

        cube[2][0][2] = cube[1][0][2]
        cube[2][1][2] = cube[1][1][2]
        cube[2][2][2] = cube[1][2][2]

        cube[1][0][2] = cube[3][2][0]
        cube[1][1][2] = cube[3][1][0]
        cube[1][2][2] = cube[3][0][0]

        cube[3][0][0] = temp[2]
        cube[3][1][0] = temp[1]
        cube[3][2][0] = temp[0]

      else:
        cube[0][0][2] = cube[3][2][0]
        cube[0][1][2] = cube[3][1][0]
        cube[0][2][2] = cube[3][0][0]

        cube[3][0][0] = cube[1][2][2]
        cube[3][1][0] = cube[1][1][2]
        cube[3][2][0] = cube[1][0][2]

        cube[1][0][2] = cube[2][0][2]
        cube[1][1][2] = cube[2][1][2]
        cube[1][2][2] = cube[2][2][2]

        cube[2][0][2] = temp[0]
        cube[2][1][2] = temp[1]
        cube[2][2][2] = temp[2]

  for i in range(3):
    print(''.join(cube[0][i]))
