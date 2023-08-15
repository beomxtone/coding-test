import sys
input = sys.stdin.readline

#
# 14425번: 문자열 집합
# https://www.acmicpc.net/problem/14425
#
# 1. 리스트로 검사하면 3736ms
# 2. 딕셔너리는 120ms
# 3. 문자열 검사할 땐 딕셔너리를 쓰자
#
# @author  Asher Seo
#

n, m = map(int, input().split())
S = {}
for _ in range(n):
  str = input().rstrip()
  if str not in S:
    S[str] = 1

ans = 0
for _ in range(m):
  str = input().rstrip()
  if str in S: ans += 1
print(ans)
