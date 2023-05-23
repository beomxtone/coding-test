import sys
input = sys.stdin.readline
import heapq

#
# 11286번: 절댓값 힙
# https://www.acmicpc.net/problem/11286
#
# @author  Asher Seo
#

n = int(input())
q = []
for _ in range(n):
  x = int(input())
  if x == 0:
    try:
      x, sign = heapq.heappop(q)
      print(sign * x)
    except:
      print(0)
  else:
    if x > 0:
      heapq.heappush(q, (x, 1))
    else:
      heapq.heappush(q, (-1*x, -1))
