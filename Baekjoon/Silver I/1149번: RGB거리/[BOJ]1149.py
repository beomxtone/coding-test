import sys
input = sys.stdin.readline

#
# 1149번: RGB거리
# https://www.acmicpc.net/problem/1149
#
# 1. RGB 색상의 배열을 DP 배열로 활용
# 2. 각각의 색상마다 최소 비용을 저장
#
# @author  Asher Seo
#

n = int(input())
L = []
for _ in range(n):
  R, G, B = map(int, input().split())
  L.append([R, G, B])

for i in range(1, n):
  # R
  L[i][0] = min(L[i-1][1], L[i-1][2]) + L[i][0]
  # G
  L[i][1] = min(L[i-1][0], L[i-1][2]) + L[i][1]
  # B
  L[i][2] = min(L[i-1][0], L[i-1][1]) + L[i][2]

print(min(L[n-1][0], L[n-1][1], L[n-1][2]))
