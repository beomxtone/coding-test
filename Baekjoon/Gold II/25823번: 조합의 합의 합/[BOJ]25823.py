import sys
input = sys.stdin.readline

#
# 25823번: 조합의 합의 합
# https://www.acmicpc.net/problem/25823
#
# 1. ∑ (k=0 to n) (nCk)^2, 즉 nCk의 제곱의 합은 2nCn과 같다.
# 2. 구하려는 답은 (n=3 to m) 까지의 2nCn의 합이다.
# 3. 점화식 2nCn = 2(n-1)Cn-1 * (2n-1) * 2n * (n*n)^-1 이 성립한다.
# 4. (n*n)^-1을 p로 나눈 수는 페르마의 소정리에 의해 n의 2(p-2) 제곱을 p로 나눈 수와 동치이다.
#
# @author  Asher Seo
#

p = 1000000007

# 거듭제곱의 분할 정복
def pow(num, x):
  if x == 0:
    return 1
  elif x == 1:
    return num

  tmp = pow(num, x//2)
  if x%2 == 0:
    return tmp * tmp % p
  else:
    return tmp * tmp * num % p


M = int(input())
res = 6  # 4C2, n이 3일 때, 2(n-1)C(n-1) = 4C2
ans = 0

for n in range(3, M+1):
  # 2n-1
  res = (res * (2*n-1)) % p
  # 2n
  res = (res * (2*n)) % p
  # 페르마의 소정리: (n*n)^-1 mod p === n^2(p-2) mod p
  res = (res * pow(n, 2*p-4)) % p
  ans += res

print(ans % p)
