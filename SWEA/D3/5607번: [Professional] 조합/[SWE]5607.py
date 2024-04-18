import sys
input = sys.stdin.readline

p = 1234567891

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


t = int(input())
for tc in range(1, t+1):
  n, k = map(int, input().split())

  # n! * ((n-k)!k!)^(p-2) % p
  ans = fac(n) * squ(fac(n-k) * fac(k), p-2) % p
  print(f'#{tc} {ans}')
