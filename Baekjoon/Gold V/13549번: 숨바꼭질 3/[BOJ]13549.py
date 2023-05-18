import sys
input = sys.stdin.readline
from collections import deque
INF = 10**9

#
# 1504번: 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
#
# 1. 다익스트라 혹은 BFS 활용
# 2. 1초 후: X-1, X+1 / 0초 후: 2*X 의 3가지 방법을 반복문으로 BFS에서 최단경로 저장
#
# @author  Asher Seo
#

def bfs(v):
  q = deque([v])
  visited[v] = 0
  while q:
    x = q.popleft()
    if x == k:
      print(visited[x])
      break
    for i in [x-1, x+1, 2*x]:
      if i < 0 or i > 100000:
        continue
      if i == 2*x and visited[x] < visited[i]:
        visited[i] = visited[x]
        q.append(i)
      if (i == x-1 or i == x+1) and visited[x]+1 < visited[i]:
        visited[i] = visited[x] + 1
        q.append(i)

n, k = map(int, input().split())
visited = [INF] * 100001
bfs(n)
