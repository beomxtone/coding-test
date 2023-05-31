import sys
input = sys.stdin.readline

#
# 1629번: 곱셈
# https://www.acmicpc.net/problem/1629
#
# 1. 그냥 구현하면 시간 초과가 뜰 것
# 2. 짝수번 곱한다면, 절반만 곱한 값을 제곱하면 같은 값이다.
#   3-1. 예를 들어 32번 곱한다면, 16번 곱한 값을 제곱하면 된다.
#   3-2. 33번이라면, 32번 곱한 값에 한번 더 곱하면 된다.
#
# @author  Asher Seo
#

def solve(a, b, c):
  if b == 1:
    return a % c
  elif b % 2 == 0:
    return solve(a, b//2, c) ** 2 % c
  else:
    return (solve(a, b//2, c) ** 2) * a % c


A, B, C = map(int, input().split())
print(solve(A, B, C))
