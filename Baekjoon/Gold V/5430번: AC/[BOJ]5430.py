import sys
input = sys.stdin.readline
from collections import deque

#
# 5430번: AC
# https://www.acmicpc.net/problem/5430
#
# 1. R: 바라보는 방향을 변경 (queue.reverse() 사용 시 시간 초과), D: R=1이면 pop(), R=0이면 popleft()
# 2. 에러가 있는 경우 'error' 출력 후, 다음 테스트 케이스로 넘어간다.
#   i.  배열의 원소 수보다 'D'가 많을 경우
#   ii. exception 에러가 발생할 경우
# 3. queue를 reverse 상태에 따라 출력한다.
#
# @author  Asher Seo
#

t = int(input())
for _ in range(t):
  commandLine = input().rstrip().replace('RR', '')  # 'RR'이면 원래 상태와 같다.
  n = int(input())
  try:
    arr = list(map(int, input().rstrip().replace('[', '').replace(']', '').split(',')))
  except: arr = []
  queue = deque(arr)
  reverse = 0  # 0: 원래 상태, 1: 뒤집힌 상태
  error = 0  # 0: 정상, 1: 에러

  for command in commandLine:
    if command.count('D') > n:  # 배열의 원소 수보다 'D'(뽑을 값)가 많을 경우 = error
      print('error')
      error = 1
      break
    if command == 'R':
      reverse = 0 if reverse else 1
    else:
      try:
        if reverse:  # 뒤에서부터 pop
          queue.pop()
        else:  # 앞에서부터 pop
          queue.popleft()
      except:
        print('error')
        error = 1
        break
  if not error:
    if reverse: queue.reverse()  # 뒤집힌 상태면 출력 전 queue를 뒤집어준다.
    print('[' + ','.join(map(str, list(queue))) + ']')