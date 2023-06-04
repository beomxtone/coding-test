import sys
input = sys.stdin.readline

#
# 14499번: 주사위 굴리기
# https://www.acmicpc.net/problem/14499
#
# 1. 주사위를 전개도대로 구현
#
# @author  Asher Seo
#

dice = [
  ['-', 0, '-'],
  [0, 0, 0],
  ['-', 0, '-'],
  ['-', 0, '-']
]

def up(dice):
  dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

def down(dice):
  dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

def left(dice):
  dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]

def right(dice):
  dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]


n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
  
  if command == 1:
    if y+1 >= m:
      continue
    y += 1
    right(dice)
    
  elif command == 2:
    if y-1 < 0:
      continue
    y -= 1
    left(dice)
    
  elif command == 3:
    if x-1 < 0:
      continue
    x -= 1
    up(dice)
    
  else:
    if x+1 >= n:
      continue
    x += 1
    down(dice)

  if maps[x][y] != 0:
    dice[3][1] = maps[x][y]
    maps[x][y] = 0
  else:
    maps[x][y] = dice[3][1]

  print(dice[1][1])
