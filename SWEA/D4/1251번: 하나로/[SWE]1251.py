import sys
input = sys.stdin.readline

def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find(parent, a)
  b = find(parent, b)
  if a < b: parent[b] = a
  else: parent[a] = b


t = int(input())
for tc in range(1, t+1):
  # 섬의 개수 n
  n = int(input())
  inputs = [list(map(int, input().split())) for _ in range(2)]
  # 섬의 좌표
  islands = list(zip(*inputs))
  # 환경 부담 세율 e, 환경 부담금: (e * 터널 길이)^2
  e = float(input())

  edges = []
  ans = 0

  parent = [0] * n
  for i in range(n):
    parent[i] = i

  for i in range(n):
    for j in range(i+1, n):
      x = (islands[j][0] - islands[i][0]) ** 2
      y = (islands[j][1] - islands[i][1]) ** 2
      cost = (x+y) * e
      edges.append((cost, i, j))

  edges.sort()

  for edge in edges:
    cost, a, b = edge

    if find(parent, a) != find(parent, b):
      union(parent, a, b)
      ans += cost

  print(f'#{tc} {round(ans)}')
