import sys
input = sys.stdin.readline

#
# 1644번: 소수의 연속합
# https://www.acmicpc.net/problem/1644
#
# 1. N의 범위가 4,000,000 이므로 N**0.5, 최대 2,000까지 에라토스테네스의 체로 소수 판별
# 2. 2부터 N까지의 소수로 시작점을 하나씩 늘려가면서 N을 만든다.
# 3. 구한 답을 출력한다.
# 4. 정답은 맞았지만, 실제 정답을 구하는 과정에서 투포인터 알고리즘을 적용하면 더 빠를 것 같다.
#
# @author  Asher Seo
#

def primeList(n):
  isPrime = [True] * n

  m = int(n**0.5)
  for i in range(2, m+1):
    if isPrime:
      for j in range(i+i, n, i):
        isPrime[j] = False

  return [i for i in range(2, n) if isPrime[i]]


n = int(input())
primes = primeList(n+1)
ans = 0

for i in range(len(primes)):
  res = primes[i]
  for j in range(i, len(primes)):
    # res가 n이 되면 ans + 1, 다음 경우의 수 진행
    if res == n:
      ans += 1
      break

    # res가 n보다 커지면 break
    elif res > n:
      break

    # j가 i이면 같은 수를 더하므로 연속성 위배, i보다 큰 인덱스만 더한다.
    if j != i:
      res += primes[j]

print(ans)
