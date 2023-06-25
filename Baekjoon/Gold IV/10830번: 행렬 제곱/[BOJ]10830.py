import sys
input = sys.stdin.readline

#
# 10830번: 행렬 제곱
# https://www.acmicpc.net/problem/10830
#
# 1. 행렬의 짝수 제곱 A^n은 (A^2)^(n/2)로 나타낼 수 있다.
# 2. 행렬의 홀수 제곱 A^(n+1)은 (A^2)^(n/2) * A로 나타낼 수 있다.
# 3. 행렬의 제곱이 1, 즉 n이 1이면 반복문을 탈출한다.
#
# @author  Asher Seo
#

def mul(x, y):
  tmp = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        # 수가 매우 커질 수 있으니, 1000으로 나눈 나머지를 구한다.
        tmp[i][j] += x[i][k] * y[k][j] % 1000
  
  return tmp

def power(x, y):
  if y == 1:
    return x

  # squ: A^(n/2)
  squ = power(x, y//2)
  # n이 짝수이면, return A^(n/2)^2
  if y%2 == 0:
    return mul(squ, squ)
  # n이 홀수이면, return A^(n/2)^2 * A
  else:
    return mul(mul(squ, squ), x)


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = power(matrix, b)
for i in range(n):
  for j in range(n):
    print(ans[i][j]%1000, end=' ')
  print()
