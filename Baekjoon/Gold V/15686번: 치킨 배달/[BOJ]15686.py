import sys
input = sys.stdin.readline
from itertools import combinations

#
# 15686번: 치킨 배달
# https://www.acmicpc.net/problem/15686
#
# 1. 치킨 집(2)의 위치 정보를 담은 배열에서 m개를 뽑는 조합을 구한다.
# 2. 1에 따른 치킨 거리를 구한다.
# 3. 2의 최솟값을 갱신해가며 모든 값을 확인한다.
#
# @author  Asher Seo
#

# n: 도시의 크기, m: 치킨집의 개수
n, m = map(int, input().split())
# city: 도시 정보, chickens: 치킨집 정보, houses: 집 정보
city, chickens, houses = [], [], []
answer = 10**9

for i in range(n):
  city.append(list(map(int, input().split())))
  for j in range(n):
    if city[i][j] == 1:
      houses.append((i, j))
    if city[i][j] == 2:
      chickens.append((i, j))

# 치킨 집을 고르는 경우의 수만큼 반복
for chicken in combinations(chickens, m):
  # 모든 집의 치킨집까지의 최소 거리
  distSum = 0
  # 집의 수만큼 반복
  for house in houses:
    # 각 집에서 치킨집까지의 최소 거리
    dist = 9999
    # 치킨집 조합의 치킨집만큼 반복
    for i in range(m):
      # dist = min(현재값, 현재 선택된 치킨집과 집의 거리)
      dist = min(dist, abs(chicken[i][0] - house[0]) + abs(chicken[i][1] - house[1]))
    distSum += dist
  answer = min(answer, distSum)

print(answer)
