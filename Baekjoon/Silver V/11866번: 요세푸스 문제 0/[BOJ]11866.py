import sys
input = sys.stdin.readline
from collections import deque

#
# 11866번: 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
#
# 1. count가 k의 배수가 아니면 append(queue.popleft())
# 2. count가 k의 배수면 queue.popleft() 후 값 저장
# 3. queue의 길이가 0이 될 때까지 수행
#
# @author  Asher Seo
#

queue = deque()
count = 0
answer = []
n, k = map(int, input().split())
for i in range(1, n+1):
  queue.append(i)

while len(queue) > 0:
  count += 1
  if count % k != 0:
    queue.append(queue.popleft())
  else:
    answer.append(queue.popleft())

print('<' + ', '.join(map(str, answer)) + '>')