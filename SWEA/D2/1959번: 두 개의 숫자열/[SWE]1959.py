T = int(input())
for TC in range(1, T+1):

  n, m = map(int, input().split())
  Aj = list(map(int, input().split()))
  Bj = list(map(int, input().split()))

  # short sequence: Aj, long sequence: Bj
  if len(Aj) > len(Bj): Aj, Bj = Bj, Aj
    
  idx, ans = 0, 0
  
  while idx <= abs(n - m):
    res = 0
    for i in range(len(Aj)):
      res += Aj[i] * Bj[i+idx]

    ans = max(ans, res)
    idx += 1
  
  print(f'#{TC} {ans}')
