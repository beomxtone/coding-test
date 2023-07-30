import sys
input = sys.stdin.readline

#
# 11726번: 2×n 타일링
# https://www.acmicpc.net/problem/11726
#
# 1. DP 메모이제이션 문제
# 2. DP[i] = DP[i-1] + DP[i-2]
# 3. 수가 너무 커질 수 있으므로 문제에서 제시한 10007로 나눈 나머지를 저장한다.
#
# @author  Asher Seo
#

n = int(input())
DP = [0]*1001

DP[1]=1
DP[2]=2
for i in range(3,1001):
  DP[i] = (DP[i-1] + DP[i-2]) % 10007

print(DP[n])
