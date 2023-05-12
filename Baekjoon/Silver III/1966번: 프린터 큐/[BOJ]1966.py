import sys
input = sys.stdin.readline
from collections import deque

#
# 1966번: 프린터 큐
# https://www.acmicpc.net/problem/1966
#
# 1. queue의 최댓값을 저장
# 2. queue의 맨 앞 값을 추출하고, 찾는 값인 m의 값에서 1을 빼준다. (queue에서 하나를 추출했으므로 m의 위치 변경)
# 3. 최댓값과 추출한 값이 같으면 cnt 증가, 다르면 추출 값을 queue의 끝에 삽입
# 4. 최댓값 == 추출값 and m < 0 이면(찾는 값이면) 해당 cnt 출력 후 종료
#
# @author  Asher Seo
#

n = int(input())

for _ in range(n):
  n, m = map(int, input().split())
  queue = deque(list(map(int, input().split())))
  cnt = 0
  
  while queue:
    maxVal = max(queue)  # queue의 최댓값 저장
    checkNum = queue.popleft()  # queue의 맨 앞 값을 추출
    m -= 1

    if maxVal == checkNum:
      cnt += 1
      if m < 0:  # 찾는 값은 m이 음수가 된다.
        print(cnt)
        break
    else:
      queue.append(checkNum)
      if m < 0: m = len(queue) - 1  # 찾는 값이지만 출력이 되지 않았으므로 맨 뒤의 위치 저장
