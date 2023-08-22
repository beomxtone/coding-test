import sys
input = sys.stdin.readline
from itertools import combinations

#
# 1759번: 암호 만들기
# https://www.acmicpc.net/problem/1759
#
# 1. 모음은 1개 이상, 자음은 2개 이상이어야 한다.
#
# @author  Asher Seo
#

l, c = map(int, input().split())
chars = list(input().split())
chars.sort()

cases = combinations(chars, l)
vows = ['a', 'e', 'i', 'o', 'u']

for case in cases:
  # 모음, 자음의 수
  vow, con = 0, 0

  # 모음, 자음 count
  for i in range(l):
    if case[i] in vows: vow += 1
    else: con += 1

  # 모음이 1개 이상, 자음이 2개 이상인 경우 출력
  if vow >= 1 and con >= 2:
    print(''.join(case))
