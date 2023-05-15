import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

#
# 10816번: 숫자 카드 2
# https://www.acmicpc.net/problem/10816
#
# 1. 이분 탐색 라이브러리 bisect 사용
# 2. bisect_right - bisect left = 해당 요소의 수
#
# @author  Asher Seo
#

def countNum(arr, x):
  left = bisect_left(arr, x)
  right = bisect_right(arr, x)
  return right - left

n = int(input())
L1 = list(map(int, input().rstrip().split()))
L1.sort()
m = int(input())
L2 = list(map(int, input().rstrip().split()))

for i in L2:
  print(countNum(L1, i), end=' ')
