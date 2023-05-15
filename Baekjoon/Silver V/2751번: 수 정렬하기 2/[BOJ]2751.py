import sys
input = sys.stdin.readline

#
# 2751번: 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
#
# @author  Asher Seo
#

n = int(input())
L = []
for _ in range(n):
  L.append(int(input()))
L.sort()
for i in L:
  print(i)
