import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

#
# 24479번: 알고리즘 수업 - 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479
#
# @author  Asher Seo
#

def dfs(value):
  global cnt
  visited[value] = cnt
  graph[value].sort()

  for i in graph[value]:
    if visited[i] == 0:
      cnt += 1
      dfs(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

dfs(r)

for i in range(1, n+1):
  print(visited[i])