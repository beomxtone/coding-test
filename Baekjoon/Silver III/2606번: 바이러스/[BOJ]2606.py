import sys
input = sys.stdin.readline
from collections import deque

#
# 2606번: 바이러스
# https://www.acmicpc.net/problem/2606
#
# 1. 1번 컴퓨터 -> 2번, 5번 컴퓨터 -> ... => BFS 문제임을 알 수 있다.
# 2. 출력은 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 이므로, visited에서 -1을 뺀 값을 출력한다.
#
# @author  Asher Seo
#

def bfs(start):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    graph[v].sort()
    for i in graph[v]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

n = int(input())
m = int(input())
graph = [[] * _ for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

bfs(1)

cnt = -1
for i in range(1, n+1):
  if visited[i]: cnt += 1
print(cnt)