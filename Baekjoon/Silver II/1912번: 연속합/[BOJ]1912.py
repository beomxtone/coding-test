import sys
input = sys.stdin.readline

#
# 1912번: 연속합
# https://www.acmicpc.net/problem/1912
#
# 1. d[i] = nums[i] + dp[i-1] 인 경우는 세 경우가 있다.
#    i. 이전 값이 0 이상일 경우
#   ii. 현재 값이 0 이상이며, (이전 값 + 현재 값) > 현재값 인 경우
#  iii. 현재 값이 0 미만이며, (이전 값 + 현재 값) >= 0 인 경우
# 2. 1의 조건에 어긋나면 d[i] = nums[i]로 dp배열을 생성한다.
#
# @author  Asher Seo
#

n = int(input())
nums = list(map(int, input().split()))
if max(nums) <= 0:
  print(max(nums))
  exit()

dp = [nums[0]]
for i in range(1, len(nums)):
  # 이전 값이 0 이상이면
  if dp[i-1] >= 0:
    # 현재값에 이전값을 더한다.
    num = nums[i] + dp[i-1]
  # 현재 값이 음수이면서, (이전값 + 현재값)이 0 이상이면
  elif nums[i] < 0 and dp[i-1] + nums[i] >= 0:
    # 현재값에 이전값을 더한다.
    num = nums[i] + dp[i-1]
  # 현재 값이 0 이상이면서, (이전값 + 현재값)이 현재값 이상이면
  elif nums[i] >= 0 and dp[i-1] + nums[i] >= nums[i]:
    # 현재값에 이전값을 더한다.
    num = nums[i] + dp[i-1]
  # 현재값에 이전값을 더하는 조건이 아니면
  else:
    # 현재값을 그대로 dp배열에 넣는다.
    num = nums[i]
  dp.append(num)

print(max(dp))
