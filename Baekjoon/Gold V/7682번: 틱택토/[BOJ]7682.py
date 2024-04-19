import sys
input = sys.stdin.readline

#
# 7682번: 틱택토
# https://www.acmicpc.net/problem/7682
#
# 1. X는 O보다 1개 더 많거나 같다.
# 2. X가 이겼다면, X의 개수는 O+1, O가 이겼다면 X의 개수는 O
# 3. 무승부라면 모든 칸이 채워져있다.
#
# @author  Asher Seo
#

def isWin(arr, typ):
  # 가로축 확인
  if arr[0] == typ and arr[0] == arr[1] == arr[2]:
    return True
  if arr[3] == typ and arr[3] == arr[4] == arr[5]:
    return True
  if arr[6] == typ and arr[6] == arr[7] == arr[8]:
    return True
  # 세로축 확인
  if arr[0] == typ and arr[0] == arr[3] == arr[6]:
    return True
  if arr[1] == typ and arr[1] == arr[4] == arr[7]:
    return True
  if arr[2] == typ and arr[2] == arr[5] == arr[8]:
    return True
  # 대각선 확인
  if arr[0] == typ and arr[0] == arr[4] == arr[8]:
    return True
  if arr[2] == typ and arr[2] == arr[4] == arr[6]:
    return True
  
  return False


while True:
  game = input().rstrip()
  if game == 'end': break

  xCnt = game.count('X')
  oCnt = game.count('O')

  # X가 이긴 상황인지 체크
  if xCnt == oCnt + 1:
    if isWin(game, 'X'):
      # X와 O는 같이 승리 조건을 만족할 수 없음
      print('invalid') if isWin(game, 'O') else print('valid')
    else:
      # x 개수가 o+1일 땐, o가 이길 수 없음
      if isWin(game, 'O'):
        print ('invalid')
      # 꽉 찬 경우는 valid
      elif game.count('.') == 0:
        print('valid')
      # 최종 상태가 아님
      else:
        print('invalid')
  # O가 이긴 상황인지 체크
  elif xCnt == oCnt:
    if isWin(game, 'O'):
      # X와 O는 같이 승리 조건을 만족할 수 없음
      print('invalid') if isWin(game, 'X') else print('valid')
    else:
      print('invalid')
  # 이외의 경우는 모두 invalid
  else:
    print('invalid')
