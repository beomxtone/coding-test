import sys
input = sys.stdin.readline

#
# 14503번: 로봇 청소기
# https://www.acmicpc.net/problem/14503
#
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
#
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
#   2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
#
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
#   3-1. 반시계 방향으로 90도 회전한다.
#   3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#   3-3. 1번으로 돌아간다.
#
# @author  Asher Seo
#

# 순서: 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# n, m: 방의 크기 n*m
n, m = map(int, input().split())
# robot[r, c, d]: (r, c)에 위치한 d 방향을 바라보는 로봇
robot = list(map(int, input().split()))
# room: n*m 크기의 방의 정보
room = list(list(map(int, input().split())) for _ in range(n))
# cleaned: 청소한 칸의 수
cleaned = 0

# 로봇청소기 시뮬레이터 시작
while True:
  # 현재 로봇의 위치: (r, c), 로봇이 보는 방향: d
  r, c, d = robot[0], robot[1], robot[2]
  
  # 현재 위치가 청소되지 않은 경우
  if room[r][c] == 0:
    # 현재 위치를 청소한다.
    room[r][c] = -1
    cleaned += 1
  
  # 현재 위치가 이미 청소된 경우
  elif room[r][c] == -1:
    isDirty = 0
    # 주위 4칸 확인
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      # 바라본 방향이 청소되지 않은 빈칸인 경우
      if room[nr][nc] == 0:
        isDirty = 1
    
    # 주위 4칸 중 청소되지 않은 빈칸이 있을 경우
    if isDirty:
      for i in range(4):
        # 청소되지 않은 빈칸을 찾으면 더이상 방향 전환을 하지 않음
        if isDirty == 2:
          continue
        # 바라보는 방향 변경
        d -= 1
        if d == -1: d = 3
        nr = r + dr[d]
        nc = c + dc[d]
        # 바라본 방향이 청소되지 않은 빈칸일 경우
        if room[nr][nc] == 0:
          # 전진
          robot[0] = nr
          robot[1] = nc
          robot[2] = d
          isDirty = 2
    
    # 주위 4칸 중 청소되지 않은 빈칸이 없을 경우
    else:
      # 후진
      nr = r - dr[d]
      nc = c - dc[d]
      # 후진 한 곳에 벽이 있으면
      if room[nr][nc] == 1:
        # 종료
        break
      # 후진 할 수 있으면
      else:
        robot[0] = nr
        robot[1] = nc
        continue

print(cleaned)
