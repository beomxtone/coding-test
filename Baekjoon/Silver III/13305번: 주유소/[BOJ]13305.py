import sys
input = sys.stdin.readline

#
# 주유소
# https://www.acmicpc.net/problem/13305
#
# 1. 뒤의 주유소 중 현재 주유소보다 유가가 싼 주유소 중 가장 가까운 주유소를 탐색한다.
# 2. 탐색한 주유소까지 갈 수 있는 연료를 충전한다.
# 3. 현재 주유소보다 유가가 싼 주유소가 없다면 현재 주유소에서 끝까지 갈 연료를 충전한다.
#
# @author  Asher Seo
#

n = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))
location = 0
totalPrice = 0

while location < n:
  currentPrice = prices[location]
  destination = 0
  for i in range(location+1, n-1):
    if currentPrice > prices[i]:
      destination = i
      totalPrice += currentPrice * sum(dists[location:i])
      location = i
      break
  if destination == 0:
    totalPrice += currentPrice * sum(dists[location:])
    location = n

print(totalPrice)