import sys
input = sys.stdin.readline
from collections import deque
INF = 10**9

#
# 16928번: 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
#
# 1. 모든 칸은 +1부터 +6까지의 간선 정보를 가진다. (주사위의 눈 수 만큼 증가)
# 2. 사다리 칸과 뱀 칸은 +1 ~ +6의 정보를 지우고, 각각 이동하는 칸으로 간선 정보를 추가한다.
# 3. 간선 정보를 바탕으로, 1에서 100까지의 최소 경로를 BFS를 이용하여 구한다.
#
# @author  Asher Seo
#

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = 0
  while q:
    v = q.popleft()
    # 사다리거나, 뱀이거나, 99번 칸이면
    if len(graph[v]) == 1:
      # 방문할 위치의 주사위 횟수 > 현재 위치의 주사위 횟수
      if visited[graph[v][0]] > visited[v]:
        # 뱀과 사다리는 100번 칸에 있을 수 없으므로, 100번 칸 하나만 갈 수 있는 칸은 99번 칸 뿐이다.
        if graph[v][0] == 99:
          # 99번 칸이면 1을 굴려 100번 칸을 갈 수 있다.
          visited[99] = visited[v] + 1
        # 사다리 or 뱀이면
        else:
          # 큐에 사다리나 뱀을 이용할 위치 정보를 저장한다.
          q.append(graph[v][0])
          # 사다리나 뱀을 타게 되면 바로 이동하므로 그대로 visited를 갱신한다.
          visited[graph[v][0]] = visited[v]
    # 주사위를 굴리는 경우이면
    else:
      # i = +1 to +6
      for i in graph[v]:
        # 방문할 값 > 현재 값 + 1
        if visited[i] > visited[v] + 1:
          q.append(i)
          visited[i] = visited[v] + 1

# n: 사다리의 수, m: 뱀의 수
n, m = map(int, input().split())
# 100칸을 가지는 그래프 초기화
graph = [[] for _ in range(100)]

for i in range(100):
  # j = 1 to 6 = 주사위의 눈
  for j in range(1, 7):
    # 100번 칸 이상의 값은 저장하지 않는다.
    if i+j <= 99:
      # i번째 칸이 주사위를 통해 갈 수 있는 칸(i+1 to i+6)을 저장한다.
      graph[i].append(i+j)

# 최소 경로 배열
visited = [INF] * 100

for _ in range(n):
  # x, y: x번 칸에 도착하면 y번 칸으로 이동하는 사다리
  x, y = map(int, input().split())
  # index는 0부터 시작하므로 -1씩 빼서 저장한다.
  graph[x-1] = [y-1]

for _ in range(m):
  # u, v: u번 칸에 도착하면 v번 칸으로 이동하는 뱀
  u, v = map(int, input().split())
  # index는 0부터 시작하므로 -1씩 빼서 저장한다.
  graph[u-1] = [v-1]

bfs(0)
print(visited[99])
