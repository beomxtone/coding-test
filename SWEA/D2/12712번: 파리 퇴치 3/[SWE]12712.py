dx1 = [1, -1, 0, 0]
dy1 = [0, 0, 1, -1]
dx2 = [1, 1, -1, -1]
dy2 = [1, -1, 1, -1]

T = int(input())
for TC in range(1, T+1):
  n, m = map(int, input().split())
  maps = [list(map(int, input().split())) for _ in range(n)]

  ans = 0
  for i in range(n):
    for j in range(n):
      # + 모양 분사 확인
      res = maps[i][j]
      for k in range(4):
        for l in range(1, m):
          nx = i + dx1[k] * l
          ny = j + dy1[k] * l
  
          if 0<=nx<n and 0<=ny<n:
            res += maps[nx][ny]
      ans = max(ans, res)

      # x 모양 분사 확인
      res = maps[i][j]
      for k in range(4):
        for l in range(1, m):
          nx = i + dx2[k] * l
          ny = j + dy2[k] * l
  
          if 0<=nx<n and 0<=ny<n:
            res += maps[nx][ny]
      ans = max(ans, res)

  print(f'#{TC} {ans}')
