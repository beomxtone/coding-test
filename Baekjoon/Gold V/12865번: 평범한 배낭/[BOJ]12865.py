import sys
input = sys.stdin.readline

#
# 12865번: 평범한 배낭
# https://www.acmicpc.net/problem/12865
#
# 1. [물품 인덱스][무게] 로 표현할 수 있는 DP 배열을 생성
# 2. D[i][j] = max(현재 가치 + D[i-1][j-현재 무게], D[i-1][j])
# 3. 마지막 칸의 값 = 정답을 출력한다.
#
# @author  Asher Seo
#

n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n)]
items = []
for _ in range(n):
  w, v = map(int, input().split())
  items.append((w, v))

for i in range(n):
  for j in range(1, k+1):
    weight, value = items[i]
    if j < weight:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[-1][-1])
