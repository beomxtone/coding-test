import sys
input = sys.stdin.readline

#
# 11401번: 이항 계수 3
# https://www.acmicpc.net/problem/11401
#
# 1. nCk % 1,000,000,007(p)를 직접 공식을 계산하거나, DP를 활용하면 TLE or MLE
# 2. 모듈러 연산 활용, nCk % p == n! * ((n-k)!k!)^-1 % p
# 3. 페르마의 소정리 활용, a^p === a (mod p) => a^(p-2) === a^-1 (mod p) (a != 0, p = 소수, a = 정수)
# 4. 3에 따라 2의 식은 n! * ((n-k)!k!)^(p-2) % p 와 같다.
#
# @author  Asher Seo
#

p = 1000000007

# 반복문으로 팩토리얼 연산
def fac(num):
  res = 1
  for i in range(2, num+1):
    res = (res*i) % p
  return res

# 거듭제곱의 분할 정복
def squ(num, x):
  if x == 0:
    return 1
  elif x == 1:
    return num

  tmp = squ(num, x//2)
  if x%2 == 0:
    return tmp * tmp % p
  else:
    return tmp * tmp * num % p


n, k = map(int, input().split())

# n! * ((n-k)!k!)^(p-2) % p
print(fac(n) * squ(fac(n-k) * fac(k), p-2) % p)
