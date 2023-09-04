import sys
input = sys.stdin.readline

#
# 2239번: 스도쿠
# https://www.acmicpc.net/problem/2239
#
# 1. 행, 열, 3x3은 서로 다른 숫자만 와야 한다. => set or dictionary 활용
#
# @author  Asher Seo
#

def check(x, y, num):
  xs, ys = (x//3)*3, (y//3)*3
  for i in range(9):
    if num == sudoku[x][i]:
      return False
    if num == sudoku[i][y]:
      return False
    if num == sudoku[xs + (i//3)][ys + (i%3)]:
      return False
  return True
    
def solve(depth):
  # 빈 칸을 다 채우면 종료
  if depth == len(blanks):
    for i in range(9):
      print(''.join(map(str, sudoku[i])))
    sys.exit(0)

  x, y = blanks[depth]
  
  for n in range(1, 10):
    if check(x, y, n):
      sudoku[x][y] = n
      solve(depth+1)
      sudoku[x][y] = 0


sudoku, blanks = [], []
for i in range(9):
  sudoku.append(list(map(int, list(input().rstrip()))))
  for j in range(9):
    if sudoku[i][j] == 0:
      blanks.append((i, j))

solve(0)
