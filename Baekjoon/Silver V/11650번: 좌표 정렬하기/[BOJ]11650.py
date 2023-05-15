import sys
input = sys.stdin.readline

#
# 11650번: 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
#
# @author  Asher Seo
#

n = int(input())
L = []
for _ in range(n):
  x, y = map(int, input().split())
  L.append((x, y))
# sorted의 key값으로 lambda function, 우선 순위는 0번째, 1번째 인덱스로 정렬
L = sorted(L, key=lambda x : (x[0], x[1]))
for set in L:
  print(set[0], set[1])
