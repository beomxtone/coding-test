import sys
input = sys.stdin.readline

#
# 15683번: 감시
# https://www.acmicpc.net/problem/15683
#
# 1. 각 cctv의 모든 경우의 수에 대해 완전 탐색 실행
# 2. 1에서 구한 case에서 사각지대의 크기를 구해 답을 도출
#
# @author  Asher Seo
#

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cctvDirs = [
  [],
  # 1번 cctv
  [[0], [1], [2], [3]],
  # 2번 cctv
  [[0, 1], [2, 3]],
  # 3번 cctv
  [[0, 2], [0, 3], [1, 2], [1, 3]],
  # 4번 cctv
  [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
  # 5번 cctv
  [[0, 1, 2, 3]]
]

# 지도에서 cctv가 감시하는 곳을 #으로 바꾸는 함수
def watch(maps, x, y, cctvDir):
  for dir in cctvDir:
    nx, ny = x, y
    
    while True:
      nx += dirs[dir][0]
      ny += dirs[dir][1]

      if 0 <= nx < n and 0 <= ny < m:
        if maps[nx][ny] == 6:
          break
        elif maps[nx][ny] == 0:
          maps[nx][ny] = '#'

      else:
        break

# depth(cctv의 index)를 기준으로 cctv의 방향을 바꿔가며 모든 경우의 수를 구하는 함수
def check(maps, depth):
  # cctv를 끝까지 체크했으면 답을 도출
  if depth >= len(cctvs):
    global ans
    cnt = 0
    
    for i in range(n):
      for j in range(m):
        if maps[i][j] == 0: cnt += 1

    ans = min(ans, cnt)
    return

  # cctv를 끝까지 확인하지 않았으면 cctv를 돌려가며 check 재귀 실행
  x, y, cctv = cctvs[depth]
  for cctvDir in cctvDirs[cctv]:
    copiedMaps = [x[:] for x in maps]
    watch(copiedMaps, x, y, cctvDir)
    check(copiedMaps, depth+1)


n, m = map(int, input().split())
maps, cctvs = [], []
ans = 10**9

for i in range(n):
  maps.append(list(map(int, input().split())))
  for j in range(m):
    if maps[i][j] != 0:
      cctvs.append((i, j, maps[i][j]))

check(maps, 0)
print(ans)
