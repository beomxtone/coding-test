import sys
input = sys.stdin.readline
from collections import deque

#
# 10026번: 적록색약
# https://www.acmicpc.net/problem/10026
#
# 1. 적록색약이 아닌 사람과, 적록색약인 사람의 카운트를 각각 선언
# 2. BFS로 각각의 visited 배열에 따라 구역 수를 카운트
# 3. 정답을 출력한다.
#
# @author  Asher Seo
#

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, color):
  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()

    if not visited[x][y]:
      visited[x][y] = True

      for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == color:
          q.append((nx, ny))


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
ans = [0, 0]

# 적록색약이 아닌 경우
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i, j, graph[i][j])
      ans[0] += 1

# 적록색약인 경우
visited = [[False]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    # 적색과 녹색을 구분하지 못한다 = 같은 색으로 인식
    if graph[i][j] == 'G': graph[i][j] = 'R'

for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      bfs(i, j, graph[i][j])
      ans[1] += 1

print(*ans)
