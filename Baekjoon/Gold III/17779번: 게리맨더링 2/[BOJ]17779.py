import sys
input = sys.stdin.readline

#
# 17779번: 게리맨더링 2
# https://www.acmicpc.net/problem/17779
#
# 1. 기준점 (x, y)와 경계의 길이 d1, d2의 조건에 따라 모든 경우의 수를 탐색
# 2. d1, d2 >= 0, 0 <= x < x+d1+d2 <= n-1, 0 <= y-d1 < y < y+d2 <= n-1
# 3. 1에서 얻은 다섯 개의 선거구의 최대값과 최소값을 구한다.
# 4. 인구 차이의 최소값을 출력
#
# @author  Asher Seo
#

def getRes(x, y, d1, d2):
  global total
  pops = [0, 0, 0, 0, 0]

  # 1번 선거구
  c = y
  for r in range(x+d1):
    if r >= x:
      c -= 1
    pops[0] += sum(maps[r][:c+1])

  # 2번 선거구
  c = y
  for r in range(x+d2+1):
    if r > x:
      c += 1
    pops[1] += sum(maps[r][c+1:])
 
  # 3번 선거구
  c = y-d1
  for r in range(x+d1, n):
    pops[2] += sum(maps[r][:c])
    if r < x+d1+d2:
      c += 1

  # 4번 선거구
  c = y+d2-n
  for r in range(x+d2+1, n):
    pops[3] += sum(maps[r][c:])
    if r <= x+d1+d2:
      c -= 1

  # 5번 선거구
  pops[4] = total - sum(pops)

  return max(pops) - min(pops)


n = int(input())
maps = []
total = 0

for i in range(n):
  maps.append(list(map(int, input().split())))
  total += sum(maps[i])

# 기준점이 될 수 있는 경우의 수
pins = []
for i in range(n-2):
  for j in range(1, n-1):
    pins.append((i, j))

ans = 10**6
for pin in pins:
  x, y = pin
  for d1 in range(1, n-1):
    for d2 in range(1, n-1):
      # x, y, d1, d2의 조건
      if x+d1+d2 <= n-1 and 0 <= y-d1 < y < y+d2 <= n-1:
        res = getRes(x, y, d1, d2)
        ans = min(ans, res)
print(ans)
