import sys
input = sys.stdin.readline
import heapq

#
# 1655번: 가운데를 말해요
# https://www.acmicpc.net/problem/1655
#
# 1. bisect를 사용한 이분탐색으로 풀이 => 2% TLE
# 2. 우선순위 큐(max Heap, min Heap)를 활용하여 풀이
# 3. 두 힙의 크기가 같을 때, 최대힙의 최댓값이 최소힙의 최소값보다 작으면 최대힙의 최댓값은 중간값이 된다.
# 4. 최대힙에 넣은 원소가 최소힙 최소값보다 크면 최소힙 최소값과 최대힙 최대값을 바꾼다.
#
# @author  Asher Seo
#

n = int(input())
maxH, minH = [], []

for _ in range(n):
  k = int(input())
  
  if len(maxH) == len(minH):
    # 최대힙은 -를 붙여서 구현
    heapq.heappush(maxH, -k)
  else:
    heapq.heappush(minH, k)

  if not minH: print(-maxH[0])
  else:
    # 최대힙 최대값 > 최소힙 최소값인 경우, 두 값을 변경
    if -maxH[0] > minH[0]:
      x = -heapq.heappop(maxH)
      y = heapq.heappop(minH)
      heapq.heappush(maxH, -y)
      heapq.heappush(minH, x)
  
    print(-maxH[0])
