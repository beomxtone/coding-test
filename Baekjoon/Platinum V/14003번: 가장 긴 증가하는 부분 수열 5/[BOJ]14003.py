import sys
input = sys.stdin.readline
from bisect import bisect_left

#
# 14003번: 가장 긴 증가하는 부분 수열 5
# https://www.acmicpc.net/problem/14003
#
# 1. 이진 탐색 - bisect 모듈 활용
# 2. 수열 하나하나의 길이 정보를 따로 저장
# 3. 2에서 구한 정보로 입력 배열을 검사, 역순 출력
#
# @author  Asher Seo
#

n = int(input())
seq = list(map(int, input().split()))
dp = [seq[0]]
lens = [1] * n

i = 1
for num in seq[1:]:
  if num > dp[-1]:
    dp.append(num)
    lens[i] = len(dp)
  else:
    lens[i] = bisect_left(dp, num) + 1
    dp[lens[i]-1] = num
  i += 1

maxLen = max(lens)
print(maxLen)
ans = []

for i in range(n-1, -1, -1):
  if lens[i] == maxLen:
    ans.append(seq[i])
    maxLen = lens[i]-1

print(*ans[::-1])
