import sys
input = sys.stdin.readline

#
# 15650번: N과 M (2)
# https://www.acmicpc.net/problem/15650
#
# 1. 백트래킹으로 풀이
#
# @author  Asher Seo
#

L = []

def recur():
  if len(L) >= m:
    print(*L)
    return
  for i in range(1, n+1):
    if i not in L:
      if len(L) == 0 or (len(L) > 0 and i > L[-1]):
        L.append(i)
        recur()
        L.pop()

n, m = map(int, input().split())
recur()
