import sys
input = sys.stdin.readline

#
# 1654번: 랜선 자르기
# https://www.acmicpc.net/problem/1654
#
# 1. 랜선을 m만큼 잘랐을 때, n개 이상의 같은 길이의 랜선을 얻을 수 있다면 Y, 아니면 N
# 2. Y라면 최적해를 구할 때까지 start = mid + 1, N라면 end = mid - 1
#
# @author  Asher Seo
#

def binarySearch(arr, start, end):
  global answer
  while start <= end:
    # mid: 자르려는 랜선의 길이
    mid = (start + end) // 2
    # count: mid만큼 잘랐을 때, 길이 mid의 랜선의 갯수
    count = 0
    for lanLine in L:
      count += lanLine // mid
    # 자른 랜선들이 n보다 많거나 같으면
    if count >= n:
      # 랜선들의 길이가 answer보다 길면 answer에 저장
      if mid > answer: answer = mid
      # 최적해를 구할 때까지 start -> mid + 1
      start = mid + 1
    # 랜선이 부족하므로 자르는 길이를 줄임
    else:
      end = mid - 1

L = []
answer = 0

k, n = map(int, input().split())
for _ in range(k):
  L.append(int(input()))

# ZeroDivisionError) 1부터 시작
binarySearch(L, 1, max(L))
print(answer)
