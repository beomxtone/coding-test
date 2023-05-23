import sys
input = sys.stdin.readline
import heapq

#
# 11279번: 최대 힙
# https://www.acmicpc.net/problem/11279
#
# @author  Asher Seo
#

n = int(input())
q = []
for _ in range(n):
  x = int(input())
  if x == 0:
    try:
      print(-heapq.heappop(q))
    except:
      print(0)
  else:
    heapq.heappush(q, -x)
