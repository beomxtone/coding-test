import sys
input = sys.stdin.readline
from collections import deque

#
# 1260번: DFS와 BFS
# https://www.acmicpc.net/problem/1260
#
# @author  Asher Seo
#

def DFS(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if visited[i] == False:
      DFS(graph, i, visited)

def BFS(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

n, m, v = map(int, input().split())
graph = [[] * x for x in range(n+1)]
visited = [False] * (n+1)
inputs = []

for _ in range(m):
  i, j = map(int, input().split())
  inputs.append((i, j))
  
# input값 정렬
inputs = sorted(inputs, key=lambda x: (x[0], x[1]))

# 인접 리스트 생성
for set in inputs:
  i, j = set[0], set[1]
  if i not in graph[j]:
    graph[j].append(i)
  if j not in graph[i]:
    graph[i].append(j)

# 인접 리스트 안의 정점 sort
for index in graph:
  index.sort()

# BFS의 인접 리스트와 visited 배열 생성
graph2 = [x[:] for x in graph]
visited2 = visited[:]

DFS(graph, v, visited)
print()
BFS(graph2, v, visited2)