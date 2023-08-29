import sys
input = sys.stdin.readline

#
# 1197번: 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
#
# 1. Kruskal Algorithm - Union Find
#
# @author  Asher Seo
#

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(a, b):
  a = find(a)
  b = find(b)
  if a < b: parents[b] = a
  else: parents[a] = b


v, e = map(int, input().split())
# (A, B, C) = A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있음
edges = [list(map(int, input().split())) for _ in range(e)]
# cost가 낮은 순서대로 정렬
edges.sort(key=lambda x:x[2])
parents = list(range(v+1))

ans = 0
for a, b, c in edges:
  if find(a) != find(b):
    union(a, b)
    ans += c

print(ans)
