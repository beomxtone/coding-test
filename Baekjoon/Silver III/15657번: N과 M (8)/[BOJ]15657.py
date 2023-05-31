import sys
input = sys.stdin.readline

#
# 15657번: N과 M (8)
# https://www.acmicpc.net/problem/15657
#
# @author  Asher Seo
#

def recur():
  if len(temp) == m:
    print(*temp)
    return

  for i in range(n):
    if len(temp) == 0 or L[i] >= temp[-1]:
      temp.append(L[i])
      recur()
      temp.pop()


n, m = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
temp = []

recur()
