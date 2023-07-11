T = int(input())
for _ in range(T):
  TC = int(input())
  scores = list(map(int, input().split()))
  dic = dict()

  for s in scores:
    if s in dic.keys():
      dic[s] += 1
    else:
      dic[s] = 1

  max_keys = [key for key, value in dic.items() if value == max(dic.values())]

  print(f'#{TC} {max(max_keys)}')
