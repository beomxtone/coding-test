import sys
input = sys.stdin.readline

#
# 2615번: 오목
# https://www.acmicpc.net/problem/2615
#
# 1. 육목일 경우는 두 가지가 있다.
# 2. 1: 여섯 번째 돌이 같은 색일 경우
# 3. 2: -1 번째 돌이 같은 색일 경우
# 4. +주의점) 육목 판정 때, 맵을 이탈할 경우는 실패가 아닌 성공으로 체크
#
# @author  Asher Seo
#

# 아래, 오른쪽, 오른쪽 아래, 오른쪽 위
dx = [1, 0, 1, -1]
dy = [0, 1, 1, 1]

board = [list(map(int, input().split())) for _ in range(19)]
winner = 0
index = (0, 0)

for i in range(19):
  if winner: break
  
  for j in range(19):
    if winner: break
    
    if board[i][j]:
      for k in range(4):
        if winner: break
        
        nx, ny = i+dx[k], j+dy[k]
        cnt = 0

        if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
          continue

        while 0 <= nx < 19 and 0 <= ny < 19 and board[i][j] == board[nx][ny]:
          cnt += 1

          # 5개의 돌이 같은 색일 때
          if cnt == 4:
            nx += dx[k]
            ny += dy[k]

            # 6번째에 같은 돌이 있는지 확인
            if nx < 0 or ny < 0 or nx >= 19 or ny >= 19 or (0 <= nx < 19 and 0 <= ny < 19 and board[i][j] != board[nx][ny]):
              nx, ny = i-dx[k], j-dy[k]
              
              # -1번째에 같은 돌이 있는지 확인
              if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                winner = board[i][j]
                index = (i+1, j+1)
                break
              else:
                if board[i][j] != board[nx][ny]:
                  winner = board[i][j]
                  index = (i+1, j+1)
                  break

          nx += dx[k]
          ny += dy[k]

print(winner)
if winner: print(index[0], index[1])
