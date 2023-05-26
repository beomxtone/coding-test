import sys
input = sys.stdin.readline

#
# 15651번: N과 M (3)
# https://www.acmicpc.net/problem/15651
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
    L.append(i)
    recur()
    L.pop()

n, m = map(int, input().split())
recur()
