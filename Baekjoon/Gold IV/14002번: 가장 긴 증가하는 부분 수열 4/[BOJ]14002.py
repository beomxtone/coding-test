import sys
input = sys.stdin.readline

#
# 14002번: 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002
#
# 1. DP를 활용해 가장 긴 증가하는 부분수열의 길이를 구한다.
# 2. 1에서 구한 DP 배열을 역순으로 돌면서, 가장 긴 길이와 DP 값이 같으면 정답 배열에 추가한다.
# 3. 2를 0번째 index까지 완료하고 나면 역순으로 구해진 정답 배열을 다시 역순으로 출력한다.
#
# @author  Asher Seo
#

n = int(input())
seq = list(map(int, input().split()))
dp = [1 for i in range(n)]

# DP[i] = i번째 수열의 가장 긴 증가하는 부분 수열의 길이
for i in range(n):
  for j in range(i):
    if seq[i] > seq[j]:
      dp[i] = max(dp[i], dp[j]+1)

# LIS 길이 출력
print(max(dp))

ans = []
idx = max(dp)

# LIS 최대길이인 idx와 DP의 값이 같으면 정답 배열에 추가, idx를 1씩 빼준다.
for i in range(n-1, -1, -1):
  if dp[i] == idx:
    ans.append(seq[i])
    idx -= 1

# 역순으로 출력
print(*reversed(ans))
