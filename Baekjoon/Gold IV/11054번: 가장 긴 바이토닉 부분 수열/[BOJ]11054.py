import sys
input = sys.stdin.readline

#
# 11053번: 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/problem/11054
#
# 1. dp[0]은 일반적인 LIS, dp[1]은 list를 역순으로 바꾼 LIS를 저장
# 2. dp[0]에서 i번째 값의 가장 긴 바이토닉 부분수열은 dp[1]의 n-1 - i-1 의 값 중 가장 큰 값을 더한 것
#
# @author  Asher Seo
#

n = int(input())
L = list(map(int, input().split()))
d = [[1]*n, [1]*n]

# d[0] LIS
for i in range(1, n):
  for j in range(0, i):
    if L[i] > L[j]:
      d[0][i] = max(d[0][i], d[0][j] + 1)

# d[1] 감소하는 부분 수열
L.reverse()

# d[1] 역순 LIS
for i in range(1, n):
  for j in range(0, i):
    if L[i] > L[j]:
      d[1][i] = max(d[1][i], d[1][j] + 1)

# d[0]과 d[1]의 최상단 값이 같은 경우를 확인하기 위해 List 복구
L.reverse()

for i in range(n):
  lowerList = d[1][:n-i-1]
  if lowerList:
    d[0][i] += max(lowerList)
    # d[0]과 d[1]의 최상단 값이 같으면 1을 빼준다.
    if L[i] == max(lowerList):
      d[0][i] -= 1

print(max(d[0]))
