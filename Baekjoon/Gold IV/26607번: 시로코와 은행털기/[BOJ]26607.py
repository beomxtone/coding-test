import sys
input = sys.stdin.readline

#
# 26607번: 시로코와 은행털기
# https://www.acmicpc.net/problem/26607
#
# 1. sum(a) + sum(b)는 항상 x*k다.
# 2. 즉, 종합 능력치는 sum(a) * (x*k - sum(b))로 나타낼 수 있다.
# 3. sum(a)로 만들 수 있는 t값들을 확인한다.
# 4. 3에서 확인한 값들을 비교해 정답을 출력한다.
#
# @author  Asher Seo
#

def knapsack(ai, k, x):
  # k-1번째부터 1번째까지 내림차순
  for i in range(k-1, 0, -1):
    # x*k 값부터 Ai(str)까지 내림차순
    for j in range(x*k, ai-1, -1):
      # i번 뽑을 때, j를 만들 수 있는가 = i-1번 뽑을 때 j에서 현재 str을 뺀 값을 만들 수 있는가
      dp[i+1][j] = dp[i+1][j] or dp[i][j-ai]
  # 1명 뽑을 때, 현재 str는 무조건 만들 수 있다
  dp[1][ai] = 1


# n: 사람의 수, k: 뽑을 인원, x: 힘과 스피드 수치의 합
n, k, x = map(int, input().split())
strs = []
for _ in range(n):
  a, b = map(int,input().split())
  # b = k-a 이므로 배열에 저장할 필요는 없다
  strs.append(a)

# k번 뽑을 때, t(≤ x*k)를 만들 수 있는지(Boolean) 저장하는 배열
dp = [[0] * (x*k+1) for _ in range(k+1)]

# a(str)에 대해서만 함수 실행
for str in strs:
  knapsack(str, k, x)

answer = 0
for i in range(x*k+1):
  # k번 뽑을 때, i를 만들 수 있다면
  if dp[k][i]:
    # 최댓값 = a의 합 * (x*k - a의 합)
    answer = max(answer, i*(x*k-i))

print(answer)
