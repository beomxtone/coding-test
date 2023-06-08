import sys
input = sys.stdin.readline

#
# 14890번: 경사로
# https://www.acmicpc.net/problem/14890
#
# 1. 모두 같은 값이면 갈 수 있는 길이다.
# 2. 경사가 높을 경우는 경사로를 깐 이후를 -1, 낮을 경우는 경사로 깔기 전을 -1 해준다.
# 3. 1의 조건으로 2를 실행하여 갈 수 있는 길인지 확인한다.
#
# @author  Asher Seo
#

n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n*2):
  if i < n:
    way = maps[i][:]
  else:
    way = [x[i-n] for x in maps][:]

  # 모두 같은 값
  if len(set(way)) <= 1:
    ans += 1
    continue

  # 경사로를 놓는 경우
  cur = 0
  for j in range(1, n):
    if cur >= n:
      break
    if way[j] == way[0]:
      continue
    if abs(way[j] - way[cur]) > 1:
      break

    # 경사가 높은 경우
    if way[j] > way[0]:
      if j-cur < l: continue
      for k in range(j, n):
        way[k] -= 1

      cur = j

    # 경사가 낮은 경우
    else:
      flag = 0
      for k in range(j+1, j+l):
        if k >= n:
          flag = 1
          break
        if way[k] != way[j]: flag = 1
      if not flag:
        for k in range(0, j):
          way[k] -= 1
        cur = j+l

  # 경사로를 전부 둔 후, 갈 수 있는 길인지 확인
  if len(set(way)) <= 1:
    ans += 1
    continue

print(ans)
