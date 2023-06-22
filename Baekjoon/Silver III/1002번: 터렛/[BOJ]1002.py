import sys
input = sys.stdin.readline
import math

#
# 1002번: 터렛
# https://www.acmicpc.net/problem/1002
#
# 1. 두 사람의 위치가 같으면서, r1=r2=0인 경우 추가
#
# @author  Asher Seo
#

TC = int(input())
for _ in range(TC):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  if dis == 0 and r1 == r2:
    if r1 == 0:
      print(1)
    else:
      print(-1)
  elif abs(r1-r2) < dis < (r1+r2):
    print(2)
  elif dis == abs(r1-r2) or dis == r1+r2:
    print(1)
  else:
    print(0)
