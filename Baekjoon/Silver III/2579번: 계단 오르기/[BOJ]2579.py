import sys
input = sys.stdin.readline

#
# 2579번: 계단 오르기
# https://www.acmicpc.net/problem/2579
#
# 1. DP - bottom up 방식
# 2. 점화식 d[i] = d[i-2] + s[i] 와 d[i-3] + s[i-1] + s[i] 중 큰 값
# 3. 문제를 더 작게 쪼갤 수 있어야 한다.
#
# @author  Asher Seo
#

n = int(input())
s = []
for _ in range(n):
  s.append(int(input()))

# 계단이 2칸 이하면 점수 출력 후 종료
if n < 3:
  print(sum(s))
  exit()

d = [0] * n
d[0] = s[0]
d[1] = s[0] + s[1]
d[2] = max(s[0] + s[2], s[1] + s[2])
d[3] = max(d[1] + s[3], d[0] + s[2] + s[3])

for i in range(4, n):
  d[i] = max(d[i-2] + s[i], d[i-3] + s[i-1] + s[i])

print(d[n-1])
