import sys
input = sys.stdin.readline

#
# 17404번: RGB거리 2
# https://www.acmicpc.net/problem/17404
#
# 1. DP = 집의 수인 크기 n 배열을 R, G, B, 3개 만큼 생성
# 2. DP[0]: R로 시작, DP[1]: G로 시작, DP[2]: B로 시작
# 3. 마지막 집은 첫 집의 색과 달라야 한다는 조건 = 마지막 DP 배열의 같은 색을 가장 큰 값으로 설정
#
# @author  Asher Seo
#

INF = 1000*1000+1
R, G, B = 0, 1, 2

n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]

ans = INF

# i: R, G, B
for i in range(3):
  dp = [[INF]*3 for _ in range(n)]
  # 첫 번째 집을 고정
  dp[0][i] = L[0][i]

  for j in range(1, n):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + L[j][0]
    dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + L[j][1]
    dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + L[j][2]

  # 마지막 집은 첫 번째 집 색깔과 달라야 하므로 INF로 설정
  dp[-1][i] = INF

  ans = min(ans, min(dp[-1]))

print(ans)
