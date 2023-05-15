import sys
input = sys.stdin.readline

#
# 2110번: 공유기 설치
# https://www.acmicpc.net/problem/2110
#
# 1. 공유기 설치가 가능한 최소 거리: start, 최대 거리: end
# 2. count >= c 이면 최소 거리 증가, count < c 이면 최대 거리 축소
#
# @author  Asher Seo
#

def binarySearch(arr, start, end):
  while start <= end:
    # mid: 공유기를 설치할 거리
    mid = (start + end) // 2
    # 공유기가 설치된 마지막 집, 첫 번째 집으로 초기화
    router = houses[0]
    # count: 공유기를 설치한 수
    count = 1
    for i in range(1, len(houses)):
      # 공유기가 설치된 집으로부터의 거리가 mid값 이상이면 = 공유기를 설치할 수 있으면
      if houses[i] - router >= mid:
        # 공유기 설치 수를 증가시킨다.
        count += 1
        # i번째 집에 공유기를 설치한다.
        router = houses[i]
    # 공유기 설치 수가 c 이상이면
    if count >= c:
      global answer
      # 최소 거리를 증가시킨다.
      start = mid + 1
      answer = mid
    # 공유기 설치 수가 c보다 적으면
    else:
      # 최대 거리를 감소시킨다.
      end = mid - 1

houses = []
n, c = map(int, input().split())
for _ in range(n):
  houses.append(int(input()))
houses.sort()

answer = 0
binarySearch(houses, 1, houses[-1] - houses[0])
print(answer)
