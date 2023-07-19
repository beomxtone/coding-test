import sys
input = sys.stdin.readline
from collections import deque;

#
# 11003번: 최솟값 찾기
# https://www.acmicpc.net/problem/11003
#
# 1. 덱에 (index, value)의 tuple을 넣으면서, index가 L개의 범위를 벗어나면 pop
# 2. 덱의 최솟값을 min으로 비교하면 TLE 예상
# 3. 덱의 맨 뒤 값과 집어넣는 값을 비교, 집어넣는 값이 더 크면 그대로 push, 작으면 맨 뒤 값을 빼고 push
# 4. 덱의 첫 번째 index가 최소값이 된다.
#
# @author  Asher Seo
#

N, L = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()

for i in range(N):
  # deque에 넣을 값보다 작은 값을 만날 때까지 pop
  while True:
    if not q or q[-1][1] <= arr[i]:
      break
    q.pop()
  q.append((i, arr[i]))

  print(q[0][1], end=' ')

  # i <= 0 인 Ai는 무시
  if i >= L-1:
    # L 범위를 벗어나는 index를 가진 수 제거
    if q[0][0] <= i-L+1:
      q.popleft()
