import sys
input = sys.stdin.readline
from collections import deque;

#
# 1456번: 거의 소수
# https://www.acmicpc.net/problem/1456
#
# 1. A <= N^2 <= B (N은 소수) 인 N^2의 수를 찾아야 한다.
# 2. B의 범위가 10^14이므로 소수 판별 알고리즘 - 에라토스테네스의 체 사용
#
# @author  Asher Seo
#

A, B = map(int, input().split())
# int(B ** 0.5) + 1을 C라 하면, C^2은 B보다 크므로 C의 제곱수는 범위에 없기 때문에 C까지만 봐도 된다.
isPrime = [True] * (int(B ** 0.5) + 1)

# 에라토스테네스의 체: 소수 판별
for i in range(2, len(isPrime)):
  if isPrime[i]:
    for j in range(i**2, len(isPrime), i):
      isPrime[j] = False

ans = 0
for i in range(2, len(isPrime)):
  if isPrime[i]:
    tmp = i
    
    while True:
      tmp *= i
      if tmp < A: continue
      if tmp > B: break
      ans += 1

print(ans)
