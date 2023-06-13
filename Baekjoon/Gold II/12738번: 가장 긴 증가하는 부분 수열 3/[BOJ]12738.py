import sys
input = sys.stdin.readline
from bisect import bisect_left

#
# 12738번: 가장 긴 증가하는 부분 수열 3
# https://www.acmicpc.net/problem/12738
#
# 1. DP 구현 = 시간 초과
# 2. DP로 구현하게 되면 arr[i]보다 작은 dp[0 ~ i-1]의 최댓값을 항상 구해야 한다.
# 3. 2는 bisect의 bisect_left로 구할 수 있다.
#
# @author  Asher Seo
#

n = int(input())
seq = list(map(int, input().split()))
ans = [seq[0]]

for num in seq[1:]:
  # i번째 값이 DP의 마지막 값보다 크면 DP에 추가
  if num > ans[-1]:
    ans.append(num)
  # 마지막 값보다 작거나 같으면 해당 index의 값을 수정
  else:
    idx = bisect_left(ans, num)
    ans[idx] = num

print(len(ans))
