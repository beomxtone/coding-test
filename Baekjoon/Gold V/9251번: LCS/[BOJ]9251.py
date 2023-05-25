import sys
input = sys.stdin.readline

#
# 9251번: LCS
# https://www.acmicpc.net/problem/9251
#
# 1. 첫 문자열과 두번째 문자열을 각각 비교
# 2. 2차원 DP 배열을 사용해 각 자리수마다 비교한다.
# 3. DP 배열의 가장 마지막에는 최댓값이 기록된다.
#
# @author  Asher Seo
#

a = input().rstrip()
b = input().rstrip()
d = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
  for j in range(1, len(b)+1):
    if a[i-1] == b[j-1]:
      d[i][j] = d[i-1][j-1] + 1
    else:
      d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[-1][-1])
