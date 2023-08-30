import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 10**9


for perm in permutations(range(n), n):
  lastCost = graph[perm[-1]][perm[0]]
  # 마지막 도시에서 출발 도시로 갈 수 없는 경우
  if lastCost == 0:
    continue

  res = lastCost
  for i in range(n-1):
    cost = graph[perm[i]][perm[i+1]]
    res += cost
  if res <= ans: continue
  
  flag = False
  for i in range(n-1):
    cost = graph[perm[i]][perm[i+1]]
    if cost == 0:
      flag = True
      break

  # 다음 경로로 갈 수 없는 경우
  if flag: continue

  ans = min(ans, res)
print(ans)
