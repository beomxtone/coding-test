import math

TC = int(input())
for _ in range(TC):
  n, m = map(int, input().split())
  ans = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
  print(ans)