import sys
input = sys.stdin.readline

#
# 9252번: LCS 2
# https://www.acmicpc.net/problem/9252
#
# 1. 2차원 배열 DP 문제
# 2. 행과 열은 첫 번째 수열과 두 번째 수열의 알파벳을 나타낸다.
# 3. 두 알파벳이 같으면 +1, 최대값을 갱신하면 길이를 구할 수 있다.
# 4. 정답인 문자열은 DP 역추적 후에 reverse
#
# @author  Asher Seo
#

A = input().rstrip()
B = input().rstrip()
n, m = len(A), len(B)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    if A[i-1] == B[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ansLen = dp[n][m]
print(ansLen)

ans = ''
for i in range(n, 0, -1):
  for j in range(m, 0, -1):
    if dp[i][j] == ansLen and A[i-1] == B[j-1]:
      ans += A[i-1]
      ansLen -= 1
      break

print(ans[::-1])
