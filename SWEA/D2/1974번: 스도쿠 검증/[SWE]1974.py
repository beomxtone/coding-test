def checkLine(x):
  if len(set(sudoku[x])) != 9 or len(set(list(i[x] for i in sudoku))) != 9:
    return False
  return True

def checkRect(x, y):
  res = []
  x, y = x//3, y//3

  for i in range(x*3, x*3+3):
    for j in range(y*3, y*3+3):
      res.append(sudoku[i][j])

  if len(set(res)) != 9:
    return False
  return True


T = int(input())
for TC in range(1, T+1):
  sudoku = [list(map(int, input().split())) for _ in range(9)]
  isFail = 0
  
  for i in range(9):
    if not checkLine(i):
      isFail = 1
      break
    for j in range(9):
      if not checkRect(i, j):
        isFail = 1
        break

  print(f'#{TC}', end=' ')
  print(1 if not isFail else 0)
