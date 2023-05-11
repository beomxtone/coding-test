import sys
input = sys.stdin.readline
from collections import deque

#
# 2164번: 카드2
# https://www.acmicpc.net/problem/2164
#
# 1. popleft()
# 2. append(popleft())
# 3. 1과 2의 과정을 카드가 하나 남을 때까지 반복
#
# @author  Asher Seo
#

queue = deque()
n = int(input())
for i in range(1, n+1):
  queue.append(i)

while len(queue) > 1:
  queue.popleft()
  queue.append(queue.popleft())
print(queue[0])