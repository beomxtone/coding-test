def solve(x, y):
  res = 0
  for i in range(x, x+M):
    for j in range(y, y+M):
      res += board[i][j]

  return res


T = int(input())

for TC in range(1, T+1):
  N, M = map(int, input().split())
  board = [list(map(int, input().split())) for _ in range(N)]
  ans = 0

  for i in range(N-M+1):
    for j in range(N-M+1):
      ans = max(ans, solve(i, j))

  print(f'#{TC} {ans}')
