import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#
# 2667번: 단지번호붙이기
# https://www.acmicpc.net/problem/2667
#
# 1. DFS를 사용하여 풀이
# 2. 값이 1인 타일 중에서 -> 방문하지 않은 타일: 1, 방문한 타일: 0
#
# @author  Asher Seo
#

def dfs(x, y):
  global apart
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    apart += 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

apart, cnt = 0, 0
num = []

for i in range(n):
  for j in range(n):
    if dfs(i, j):
      num.append(apart)
      cnt += 1
      apart = 0
      
num.sort()
print(cnt)
for i in num:
  print(i)