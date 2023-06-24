import sys
input = sys.stdin.readline

#
# 17143번: 낚시왕
# https://www.acmicpc.net/problem/17143
#
# 1. 낚시왕은 오른쪽으로 한 칸씩 이동하며 같은 열, 작은 행의 상어를 한 마리 잡는다.
# 2. 상어는 주어진 속력에 따라 칸을 이동, 벽을 마주치면 반대 방향으로 이동한다.
# 3. 이동이 끝난 후, 한 칸에 둘 이상의 상어가 있으면 가장 큰 상어만 남는다.
# 4. 낚시왕이 잡는 상어 크기의 합을 출력
#
# @author  Asher Seo
#

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

r, c, m = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]
sharks = {}
for _ in range(m):
  x, y, s, d, z = map(int, input().split())
  graph[x-1][y-1] = z
  sharks[z] = [x-1, y-1, s, d]

fisher = -1
catched = []
while fisher+1 < c:
  # 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
  fisher += 1

  # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
  for i in range(r):
    if graph[i][fisher] != 0:
      shark = graph[i][fisher]
      catched.append(shark)
      del sharks[shark]
      graph[i][fisher] = 0
      break

  # 3. 상어가 이동한다.
  moves = {}
  graph = [[0 for _ in range(c)] for _ in range(r)]
  for shark in sharks:
    x, y, s, d = sharks[shark]

    if d == 1 or d == 2:
      if r > 1:
        s %= 2*(r-1)
      else:
        s = 0
    else:
      if c > 1:
        # 2(c-1)만큼 앞으로 가면 원래 자리, 원 방향값으로 돌아온다.
        s %= 2*(c-1)
      else:
        s = 0

    nx, ny = x, y
    for _ in range(s):
      nx += dx[d-1]
      ny += dy[d-1]
      if nx < 0 or ny < 0 or nx >= r or ny >= c:
        if d == 1 or d == 2:
          d = 2 if d == 1 else 1
        else:
          d = 4 if d == 3 else 3

        # 벽을 만났을 때, 방향 전환
        if nx < 0: nx += 2
        elif nx >= r: nx -= 2
        elif ny < 0: ny += 2
        elif ny >= c: ny -= 2

    if (nx, ny) not in moves:
      moves[(nx, ny)] = [shark]
    else:
      moves[(nx, ny)].append(shark)

    sharks[shark] = nx, ny, s, d

  # 같은 칸에 상어가 여러마리이면 큰 상어만 남는다.
  for pos in moves:
    if len(moves[pos]) > 1:
      res = 0
      for size in moves[pos]:
        if size > res:
          if res != 0:
            del sharks[res]
          res = size
        else:
          del sharks[size]

  # 상어의 위치 정보 갱신
  for shark in sharks:
    x, y, s, d = sharks[shark]
    graph[x][y] = shark

print(sum(catched))
