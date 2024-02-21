import sys
input = sys.stdin.readline

#
# 2644번: 촌수계산
# https://www.acmicpc.net/problem/2644
#
# 1. 연결 그래프 DFS
#
# @author  Asher Seo
#

def dfs(graph, v, visited, depth):
  global b
  if v == b:
    print(depth)
    sys.exit()
  
  visited[v] = True
  for node in graph[v]:
    if not visited[node]:
      dfs(graph, node, visited, depth+1)


n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
graph = dict()
for _ in range(m):
  key, child = map(int, input().split())
  if key not in graph:
    graph[key] = []
  if child not in graph:
    graph[child] = []
  graph[key].append(child)
  graph[child].append(key)

dfs(graph, a, visited, 0)
print(-1)
