import sys
input = sys.stdin.readline
from collections import deque

#
# 24445번: 알고리즘 수업 - 너비 우선 탐색 2
# https://www.acmicpc.net/problem/24445
#
# @author  Asher Seo
#

def bfs(start):
  global cnt
  queue = deque([start])
  visited[start] = cnt
  cnt += 1

  while queue:
    v = queue.popleft()
    graph[v].sort(reverse=True)
    for i in graph[v]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = cnt
        cnt += 1

n, m, r = map(int, input().split())
graph = [[] * _ for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

bfs(r)

for i in range(1, n+1):
  print(visited[i])