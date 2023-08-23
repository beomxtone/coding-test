import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

#
# 17471번: 게리맨더링
# https://www.acmicpc.net/problem/17471
#
# @author  Asher Seo
#

def check(arr):
  q = deque()
  visited = [False for _ in range(n)]
  q.append(arr[0])
  visited[arr[0]] = True

  while q:
    v = q.popleft()

    for i in range(len(graph[v])):
      if graph[v][i] == False: continue
      if i not in arr: continue
      if not visited[i]:
        visited[i] = True
        q.append(i)

  return visited.count(True) == len(arr)

def count(arr):
  res = 0
  for n in arr:
    res += persons[n]
  return res


n = int(input())
persons = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(n)]

graph = [[False]*n for _ in range(n)]
idx = 0
for info in infos:
  for i in range(1, len(info)):
    graph[idx][info[i]-1] = True
  idx += 1

ans = 10**9

for i in range(1, n):
  for first in combinations(range(n), i):
    first = list(first)
    second = list(set(range(n)) - set(first))
    
    if check(first) and check(second):
      res = abs(count(first) - count(second))
      ans = min(ans, res)

print(ans if ans != 10**9 else -1)
