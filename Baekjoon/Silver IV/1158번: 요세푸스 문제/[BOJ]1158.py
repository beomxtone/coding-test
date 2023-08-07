import sys
input = sys.stdin.readline
from collections import deque

#
# 1158번: 요세푸스 문제
# https://www.acmicpc.net/problem/1158
#
# 1. 11866과 동일한 코드
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
