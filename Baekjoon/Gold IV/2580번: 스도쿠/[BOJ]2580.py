import sys
input = sys.stdin.readline

#
# 2580번: 스도쿠
# https://www.acmicpc.net/problem/2580
#
# 1. 0이면 가로, 세로, 3x3, 세 조건에 맞는 값을 작은 값부터 바꿔준다.
# 2. 차례대로 0을 찾아 바꿔주다가, 바꿀 수 있는 값이 없으면 1로 돌아가서 1의 값을 바꾼다.
#
# @author  Asher Seo
#

# 스도쿠의 조건에 맞는지 확인하는 함수
def isFine(x, y, n):
  nums = [n for n in range(1, 10)]
  # x축에 같은 값이 있는지 확인
  for i in range(9):
    if n == sudoku[x][i]:
      return False
  # y축에 같은 값이 있는지 확인
  for i in range(9):
    if n == sudoku[i][y]:
      return False
  # 3x3 칸에 같은 값이 있는지 확인
  nx, ny = x//3*3, y//3*3
  for i in range(3):
    for j in range(3):
      if sudoku[nx+i][ny+j] == n:
        return False
  # 위의 세 조건을 통과하면 True
  return True

# 빈칸마다 스도쿠를 해결
def solve(n):
  # 빈칸을 모두 해결했으면 문제를 다 푼 것
  if n == len(blanks):
    for i in range(9):
      print(*sudoku[i])
    sys.exit(0)

  x, y = blanks[n]
  for i in range(1, 10):
    # 스도쿠 조건에 맞는 값이 있으면
    if isFine(x, y, i):
      # 빈칸을 i로 바꾼다.
      sudoku[x][y] = i
      # 다음 분기 실행
      solve(n+1)
      # 다음 분기에서 스도쿠 조건에 맞는 값이 없으면 현재 분기의 빈칸 값을 0으로 돌린다.
      sudoku[x][y] = 0
  

sudoku = []
blanks = []
for i in range(9):
  sudoku.append(list(map(int, input().split())))
  for j in range(9):
    if sudoku[i][j] == 0:
      blanks.append((i, j))

solve(0)
