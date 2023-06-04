import sys
input = sys.stdin.readline

#
# 14500번: 테트로미노
# https://www.acmicpc.net/problem/14500
#
# 1. 가능한 도형을 (i, j)를 기준으로 구현
# 2. 좌표마다 1에서 구한 도형들을 넣고 최대값 갱신
#
# @author  Asher Seo
#

tetris = [
  [(0, 0), (0, 1), (1, 0), (1, 1)],  # Omino
  
  [(0, 0), (0, 1), (0, 2), (0, 3)],  # Imino1
  [(0, 0), (1, 0), (2, 0), (3, 0)],  # Imino2
  
  [(0, 0), (0, 1), (1, 1), (1, 2)],  # Zmino1
  [(0, 1), (1, 0), (1, 1), (2, 0)],  # Zmino2
  
  [(0, 1), (0, 2), (1, 0), (1, 1)],  # Smino1
  [(0, 0), (1, 0), (1, 1), (2, 1)],  # Smino2
  
  [(0, 1), (1, 1), (2, 1), (2, 0)],  # Jmino1
  [(0, 0), (1, 0), (1, 1), (1, 2)],  # Jmino2
  [(0, 0), (0, 1), (1, 0), (2, 0)],  # Jmino3
  [(0, 0), (0, 1), (0, 2), (1, 2)],  # Jmino4
  
  [(0, 0), (1, 0), (2, 0), (2, 1)],  # Lmino1
  [(0, 0), (0, 1), (0, 2), (1, 0)],  # Lmino2
  [(0, 0), (0, 1), (1, 1), (2, 1)],  # Lmino3
  [(0, 2), (1, 0), (1, 1), (1, 2)],  # Lmino4
  
  [(0, 0), (0, 1), (0, 2), (1, 1)],  # Tmino1
  [(0, 1), (1, 0), (1, 1), (2, 1)],  # Tmino2
  [(0, 1), (1, 0), (1, 1), (1, 2)],  # Tmino3
  [(0, 0), (1, 0), (1, 1), (2, 0)]   # Tmino4
]


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(n):
  for j in range(m):
    for mino in tetris:
      flag = 1
      sumBlock = 0
      
      for k in range(4):
        if 0 <= i+mino[k][0] < n and 0 <= j+mino[k][1] < m:
          x, y = i+mino[k][0], j+mino[k][1]
          sumBlock += maps[x][y]
        else:
          flag = 0
          break

      if flag:
        answer = max(answer, sumBlock)

print(answer)
