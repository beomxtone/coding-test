import sys
input = sys.stdin.readline

#
# 1300번: K번째 수
# https://www.acmicpc.net/problem/1300
#
# 1. m 이하의 수의 개수 >= k 이면 k중 가장 작은 값이 k번째 수가 된다.
# 2. i번째 열에서 m 이하의 수의 개수 = min(m//i, n) 임을 알 수 있다.
#
# @author  Asher Seo
#

def binarySearch(target, start, end):
  while start <= end:
    # mid: m 이하의 수의 개수를 구할 때의 m
    mid = (start + end) // 2
    # count: m 이하 수의 개수
    count = 0
    for i in range(1, n+1):
      # i번째 열 중에서 m 이하 수의 개수를 count에 더함
      count += min(mid//i, n)
    # m 이하의 수가 k 이상이면
    if count >= target:
      global answer
      answer = mid
      # 최댓값을 m으로 감소시킨다.
      end = mid - 1
    # m 이하의 수가 k보다 적으면
    else:
      # 최솟값을 m으로 증가시킨다.
      start = mid + 1

n = int(input())
k = int(input())
answer = 0
binarySearch(k, 1, min(10**9, n**2))
print(answer)
