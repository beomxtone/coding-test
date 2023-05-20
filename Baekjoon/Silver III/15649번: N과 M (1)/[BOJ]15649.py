import sys
input = sys.stdin.readline
from itertools import permutations

#
# 15649번: N과 M (1)
# https://www.acmicpc.net/problem/15649
#
# @author  Asher Seo
#

n, m = map(int, input().split())
L = [x for x in range(1, n+1)]
p = list(permutations(L, m))

for i in p:
  for j in i:
    print(j, end=' ')
  print()
