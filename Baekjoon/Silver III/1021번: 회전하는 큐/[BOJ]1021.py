import sys
input = sys.stdin.readline
from collections import deque

#
# 1021번: 회전하는 큐
# https://www.acmicpc.net/problem/1021
#
# 1. 뽑아내려는 값이 나올 때까지 rotate(-1)과 rotate(1)을 수행하고, 각각 기록한다.
# 2. min(cnt1, cnt2) 값을 cnt에 더하고, 뽑아내려는 값을 뽑아낸다.
# 3. 뽑아내려는 원소가 없을 때까지 반복한다.
#
# @author  Asher Seo
#

n, m = map(int, input().split())
queue1 = deque(range(1, n+1))  # rotate(-1)을 수행할 queue
queue2 = deque(range(1, n+1))  # rotate(1)을 수행할 queue
values = list(map(int, input().split()))
cnt = 0

for value in values:
  cnt1, cnt2 = 0, 0
  while value != queue1[0]:
    cnt1 += 1  # 왼쪽으로 한 칸 이동시킨 횟수
    queue1.rotate(-1)
  while value != queue2[0]:
    cnt2 += 1  # 오른쪽으로 한 칸 이동시킨 횟수
    queue2.rotate(1)
  if value == queue1[0]:  # queue의 첫 번째 값과 뽑아내려는 값이 같으면 뽑아낸다.
    queue1.popleft()
    queue2.popleft()
  cnt += min(cnt1, cnt2)
print(cnt)