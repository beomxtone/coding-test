import sys
input = sys.stdin.readline

#
# 1920번: 수 찾기
# https://www.acmicpc.net/problem/1920
#
# 1. 이분 탐색 구현
#
# @author  Asher Seo
#

def binarySearch(arr, start, end, target):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return 0

n = int(input())
L1 = list(map(int, input().rstrip().split()))
L1.sort()
m = int(input())
L2 = list(map(int, input().rstrip().split()))

for i in L2:
  print(binarySearch(L1, 0, n-1, i))
