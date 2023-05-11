import sys
input = sys.stdin.readline

# Greedy Algorithm
#   정당성 분석) 빨리 인출하는 사람을 먼저 처리하는 것이 최적의 해인가?
#          => 그렇다. 뒤로 갈수록 앞의 처리 시간을 더하기 때문
# 1. Pi 값이 낮은 순서대로 정렬
# 2. P1 + (P1 + P2) + (P1 + P3) ... 출력

n = int(input())
times = list(map(int, input().split()))
times.sort()
totalTime = 0

for i in range(n):
  totalTime += sum(times[:i+1])

print(totalTime)