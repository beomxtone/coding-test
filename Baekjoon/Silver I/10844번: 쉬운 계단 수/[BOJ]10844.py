import sys
input = sys.stdin.readline

#
# 10844번: 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
#
# 1. 아이디어: 맨 뒤 숫자의 앞 숫자는 맨 뒤의 수의 +1, -1 값이다.
# 2. d[i][j]를 10^i 자리의 끝이 j인 수라고 가정해보자
# 3. j가 0 또는 9가 아닐 때, d[i][j] = d[i-1][j-1] + d[i-1][j+1] 이다.
#
# @author  Asher Seo
#

n = int(input())
d = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(1, n):
  temp = []
  # 맨 뒤의 수가 0일 경우, 그 앞은 1만 올 수 있다.
  temp.append(d[i-1][1] % (10**9))
  for j in range(1, 9): # j = 1~8
    temp.append((d[i-1][j-1] + d[i-1][j+1]) % (10**9))
  # 맨 뒤의 수가 9일 경우, 그 앞은 8만 올 수 있다.
  temp.append(d[i-1][8] % (10**9))
  d.append(temp)

print(sum(d[n-1]) % (10**9))
