T = int(input())
for TC in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  ans = [[] for _ in range(3)]
  
  # 90도 회전
  res = list(zip(*arr[::-1]))
  ans[0] = res

  # 180도 회전
  res = list(zip(*res[::-1]))
  ans[1] = res

  # 270도 회전
  res = list(zip(*res[::-1]))
  ans[2] = res

  print(f'#{TC}')
  for i in range(N):
    for j in range(3):
      print(''.join(map(str, ans[j][i])), end=' ')
    print()
