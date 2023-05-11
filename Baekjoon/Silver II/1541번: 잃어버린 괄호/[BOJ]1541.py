import sys
input = sys.stdin.readline

# Greedy Algorithm
#   Idea: 음수 항을 최댓값으로 만든다. => '-'를 기준으로 split으로 나눈다.
#   정당성 분석) 음수 값을 크게 만드는 것이 최적의 해인가?
#          => 그렇다. 음수가 커질 수록 최소에 가까워지기 때문
# 1. 음수 항이 나오면 split으로 나눈다.
# 2. 첫 항에서 나머지 항을 뺀다.
#  * 첫 시작은 항상 숫자이기 때문에, 음수 시작을 고려할 필요는 없다.

formula = input().rstrip().split('-')
nums = []

for i in formula:
  subFormula = i.split('+')
  sumSub = 0
  for j in subFormula:
    sumSub += int(j)
  nums.append(sumSub)

answer = nums[0]
for i in range(1, len(nums)):
  answer -= nums[i]
print(answer)