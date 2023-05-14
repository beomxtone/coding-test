import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#
# 1012번: 유기농 배추
# https://www.acmicpc.net/problem/1012
#
# 1. DFS를 사용하여 풀이
# 2. 값이 1인 타일 중에서 -> 방문하지 않은 타일: 1, 방문한 타일: 0
#
# @author  Asher Seo
#

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
  if x < 0 or x >= m or y < 0 or y >= n:
    return False
  if graph[y][x] == 1:
    graph[y][x] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)
    return True
  return False

T = int(input())
for _ in range(T):
  m, n, k = map(int, input().split())
  graph = [[0 for _ in range(m)] for _ in range(n)]
  cnt = 0
  for _ in range(k):
    u, v = map(int, input().split())
    graph[v][u] = 1

  for i in range(m):
    for j in range(n):
      if dfs(i, j):
        cnt += 1
  print(cnt)
