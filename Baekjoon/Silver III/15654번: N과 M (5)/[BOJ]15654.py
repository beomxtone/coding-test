import sys
input = sys.stdin.readline

#
# 15654번: N과 M (5)
# https://www.acmicpc.net/problem/15654
#
# @author  Asher Seo
#

def recur():
  if len(temp) == m:
    print(*temp)
    return

  for i in range(n):
    if L[i] not in temp:
      temp.append(L[i])
      recur()
      temp.pop()


n, m = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
temp = []

recur()
