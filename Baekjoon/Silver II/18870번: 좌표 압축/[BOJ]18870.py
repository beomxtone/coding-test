import sys
input = sys.stdin.readline

#
# 18870번: 좌표 압축
# https://www.acmicpc.net/problem/18870
#
# 1. Dictionary 사용 { key: 숫자, value: 정렬된 index }
#
# @author  Asher Seo
#

n = int(input())
coord = {}
L = list(map(int, input().rstrip().split()))

sortL = sorted(L)
cnt = 0
for num in sortL:
  if num not in coord:
    coord[num] = cnt
    cnt += 1

for i in L:
  print(coord[i], end=' ')
