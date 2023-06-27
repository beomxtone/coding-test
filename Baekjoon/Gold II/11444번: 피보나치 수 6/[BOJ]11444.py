import sys
input = sys.stdin.readline

#
# 11444번: 피보나치 수 6
# https://www.acmicpc.net/problem/11444
#
# 1. DP를 활용하면 입력값이 1,000,000,000,000,000,000 이하므로 메모리 초과
# 2. 피보나치 규칙을 행렬로 변환하여 풀이
# 3. [[F(n+1), F(n)], [F(n), F(n-1)]] = [[1, 1], [1, 0]]^n
# 4. [BOJ] 10830번: 행렬 제곱의 방법 사용, 결과값의 [0][1] 출력
#
# @author  Asher Seo
#

def mul(x, y):
  tmp = [[0]*2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        # 수가 매우 커질 수 있으니, 1000000007으로 나눈 나머지를 구한다.
        tmp[i][j] += x[i][k] * y[k][j] % 1000000007
  
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


n = int(input())
matrix = [[1, 1], [1, 0]]

ans = power(matrix, n)
print(ans[0][1] % 1000000007)
