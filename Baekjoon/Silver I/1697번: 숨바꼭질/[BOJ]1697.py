import sys
input = sys.stdin.readline
from collections import deque

#
# 1697번: 숨바꼭질
# https://www.acmicpc.net/problem/1697
#
# 1. BFS - 노드마다 최단 거리를 구할 수 있다.
# 2. 각 노드는 n-1, n+1, n*2 노드에 접근할 수 있다.
#
# @author  Asher Seo
#

def bfs(v):
  queue = deque([v])
  while queue:
    x = queue.popleft()
    if x == k:
      print(visited[x])
      break
    for i in [x-1, x+1, x*2]:
      if 0 <= i <= maxNum and visited[i] == 0:
        queue.append(i)
        visited[i] = visited[x] + 1

n, k = map(int, input().split())
maxNum = 100000
visited = [0] * (maxNum + 1)

bfs(n)
