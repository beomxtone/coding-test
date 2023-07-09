import sys
input = sys.stdin.readline
from collections import deque

#
# 13913번: 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
#
# 1. BFS로 수빈이가 이동 가능한 x-1, x+1, 2*x 경로로 탐색
# 2. visited 배열에 depth 뿐 아니라 parent를 추가해 상위 요소 link
# 3. x와 k가 같으면 depth를 출력, parent를 따라 이동 경로를 출력
#
# @author  Asher Seo
#

INF = 10**9

def bfs(v):
  q = deque([v])
  visited[v] = (0, v)
  
  while q:
    x = q.popleft()

    # 수빈이의 위치가 동생의 위치와 같으면 종료
    if x == k:
      depth, parent = visited[x]
      # 수빈이가 동생을 찾는 가장 빠른 시간 출력
      print(depth)

      # 수빈이의 이동 경로 초기화
      ans = [k, parent] if k != parent else [k]
      while True:
        if parent == n: break
        parent = visited[parent][1]
        ans.append(parent)

      # 역순으로 출력
      print(*reversed(ans))

    # 걸으면 x-1, x+1, 순간이동하면 2*x
    for i in [x-1, x+1, 2*x]:
      if i < 0 or i > 100000:
        continue
      if i == 2*x and visited[x][0]+1 < visited[i][0]:
        visited[i] = (visited[x][0] + 1, x)
        q.append(i)
      if (i == x-1 or i == x+1) and visited[x][0]+1 < visited[i][0]:
        visited[i] = (visited[x][0] + 1, x)
        q.append(i)

n, k = map(int, input().split())
# (depth, parent)
visited = [(INF, -1)] * 100001
bfs(n)
