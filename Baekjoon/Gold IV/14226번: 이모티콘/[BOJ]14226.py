import sys
input = sys.stdin.readline
from collections import deque

#
# 14226번: 이모티콘
# https://www.acmicpc.net/problem/14226
#
# 1. BFS로 1) 이모티콘 모두 복사, 2) 이모티콘 모두 붙여넣기, 3) 화면의 이모티콘 하나 삭제 의 3가지 과정 수행
# 2. visited 배열을 dictionary로 선언, (화면, 클립보드)로 구성
# 3. 화면에 이모티콘이 S개가 되면 종료
#
# @author  Asher 

S = int(input())
q = deque()
# (current emoticons, clip board)
q.append((1, 0))
visited = dict()
# 현재 상태 초기화
visited[(1, 0)] = 0

while q:
  emos, clip = q.popleft()

  # 화면의 이모티콘이 S개가 되면 종료
  if emos == S:
    print(visited[(emos, clip)])
    break

  # 이모티콘 모두 복사
  if (emos, emos) not in visited.keys():
    visited[(emos, emos)] = visited[(emos, clip)] + 1
    q.append((emos, emos))

  # 이모티콘 모두 붙여넣기
  if clip > 0 and (emos+clip, clip) not in visited.keys():
    visited[(emos+clip, clip)] = visited[(emos, clip)] + 1
    q.append((emos+clip, clip))

  # 화면에서 이모티콘 하나 삭제
  if emos > 0 and (emos-1, clip) not in visited.keys():
    visited[(emos-1), clip] = visited[(emos, clip)] + 1
    q.append((emos-1, clip))
